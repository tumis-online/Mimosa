import argparse
import asyncio
import base64
import hashlib
import logging
import os.path

import aiofiles
import yaml
from yaml.loader import SafeLoader
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


DEFAULT_CONFIG_FILE = "gql-config.yml"
GQL_SINGLE_UPLOAD_MUTATION = '''
      mutation($file: Upload!) {
        singleUpload(file: $file) {
          id
        }
      }
    '''
GQL_MULTIPLE_UPLOAD_MUTATION = '''
      mutation($files: [Upload!]!) {
        multipleUpload(files: $files) {
          id
        }
      }
    '''

MAX_LOCAL_FILE_SIZE = 40


def load_gql_api_endpoint(config_file=None) -> str:
    """Loads api endpoint url from yml config file.
    :return api endpoint url
    """
    # Config file provided?
    if config_file is None:
        config_file = DEFAULT_CONFIG_FILE

    # Open and load the config file and return api url
    with open(config_file, 'r') as config:
        data = yaml.load(config, Loader=SafeLoader)
        logging.info(data)
        error: bool = False
        if data["url"] is not None:
            return data["url"]
        for val in "host", "port", "suffix":
            if data[val] is None:
                logging.error(f"Missing {val} in GraphQL client configuration file.")
                error = True
        if error:
            logging.error("Configuration file is not valid. No api endpoint provided.")
    host = data["host"]
    port = data["port"]
    suffix = data["suffix"]
    api_endpoint = f"http://{host}:{str(port)}{suffix}"
    return api_endpoint


async def send_graphql_request(session, graphql_request: str) -> str:
    """Executing a single query.
    :return result of GraphQL request
    """
    query = gql(graphql_request)
    result = await session.execute(query)
    return result


def send_multiple_graphql_request_files(session, graphql_files: list) -> str:
    """Send multiple query files.
    :return result of GraphQL request
    """
    logging.info(f"Send multiple GraphQL requests from multiple files: {graphql_files}. {session}")
    query = gql(GQL_MULTIPLE_UPLOAD_MUTATION)
    files: list = []
    for f_path in graphql_files:
        file = open(f_path, "rb")
        files.append(file)

    params = {"files": graphql_files}

    result = session.execute(
        query, variable_values=params, upload_files=True
    )

    for file in files:
        file.close()
    return result


def send_graphql_request_file(session, graphql_file: str) -> str:
    """Send a query file.
    :return result of GraphQL request
    """
    logging.info(f"Sending GraphQL request from file: {graphql_file}. {session}")
    file_size = os.path.getsize(graphql_file)
    if file_size > MAX_LOCAL_FILE_SIZE:
        return stream_graphql_request_file(graphql_file)
    query = gql(GQL_SINGLE_UPLOAD_MUTATION)

    with open(graphql_file, "rb") as file:
        params = {"file": file}

        result = session.execute(
            query, variable_values=params, upload_files=True
        )
    return result


def stream_graphql_request_file(session, graphql_file: str) -> str:
    """Use streaming for big file to limit amount of memory used.
    :return result of GraphQL request
    """
    logging.info(f"Streaming GraphQL request from file: {graphql_file}. {session}")
    query = gql(GQL_MULTIPLE_UPLOAD_MUTATION)

    async def file_sender(file_name):
        async with aiofiles.open(file_name, 'rb') as f:
            chunk = await f.read(64 * 1024)
            while chunk:
                yield chunk
                chunk = await f.read(64 * 1024)

    params = {"file": file_sender(file_name=graphql_file)}

    result = session.execute(
        query, variable_values=params, upload_files=True
    )
    return result


def __generate_password_hash(password: str) -> bytes:
    """Generates password hash on client side for BCO to log in analogous to BCO doc:
    https://basecubeone.org/developer/addon/bco-api-graphql.html#how-to-generate-the-password-hash-on-client-side.
    1. Encoding the plain text password as UTF16
    2. Compute a hash of the UTF16 bytes by using the SHA-256 hash generator algorithm
    3. Encode the result as Base64 and pass it to the login method as passwordHash.
    """
    hashed_password = base64.b64encode(hashlib.sha256(password.encode("utf-16")).digest())
    return hashed_password


async def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-v', '--verbose', help='', action='store_true')
    parser.add_argument('-d', '--debug', help='', action='store_true')
    parser.add_argument('-c', '--config', help='', nargs=1)
    args = parser.parse_args()

    level = logging.DEBUG if hasattr(args, 'debug') else logging.INFO
    logging.basicConfig(filename='graphql_client.log', encoding='utf-8', level=level)

    api_endpoint = load_gql_api_endpoint(args.config)
    transport = AIOHTTPTransport(url=api_endpoint, headers={'Authorization': 'token'})
    '''
    headers={'Authorization': 'token'} ?
    Alternative:  cookies={"cookie1": "val1"}
    Alternative: Cookie Jar
    jar = aiohttp.CookieJar()
    transport = AIOHTTPTransport(url=url, client_session_args={'cookie_jar': jar})
    '''

    # Using `async with` on the client will start a connection on the transport
    # and provide a `session` variable to execute queries on this connection
    async with Client(
        transport=transport,
        fetch_schema_from_transport=True,
    ) as session:
        # result = send_graphql_request(session, "")

        result = send_graphql_request_file(session, "login_query.graphql")
        logging.info(result)


asyncio.run(main())
