import aiohttp.client_exceptions
import argparse
import asyncio
import base64
import hashlib
import os.path

import yaml
import logging

from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.requests import log as requests_logger
from yaml.loader import SafeLoader

from bco.api.graphql.client.gql_client_handler import GraphQLClientHandler, parse_graphql_file

DEFAULT_CONFIG_FILE = "gql-config.yml"
"""GraphQL Requests"""
LOGIN_QUERY_FILE = "requests/queries/login_query.graphql"
GET_LIGHTS_QUERY_FILE = "requests/queries/get_lights_query.graphql"
SWITCH_LIGHT_MUTATION_FILE = "requests/mutations/switch_light_mutation.graphql"


def load_gql_api_endpoint(config_file=None) -> str:
    """Loads api endpoint url from yml config file.
    :return api endpoint url
    """
    # Config file provided?
    if config_file is None:
        config_file = DEFAULT_CONFIG_FILE
    if not os.path.exists(config_file):
        logging.error(f"Config file {config_file} could not be located.")
    # Open and load the config file and return api url
    with open(config_file, 'r') as config:
        data = yaml.load(config, Loader=SafeLoader)
        error: bool = False
        if "url" in data and data["url"] is not None:
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
    logging.info(f"Establish GraphQL Client connection to {api_endpoint}...")
    return api_endpoint


def __generate_password_hash(password: str) -> bytes:
    """Generates password hash on client side for BCO to log in analogous to BCO doc:
    https://basecubeone.org/developer/addon/bco-api-graphql.html#how-to-generate-the-password-hash-on-client-side.
    1. Encoding the plain text password as UTF16
    2. Compute a hash of the UTF16 bytes by using the SHA-256 hash generator algorithm
    3. Encode the result as Base64 and pass it to the login method as passwordHash.
    """
    hashed_password = base64.b64encode(hashlib.sha256(password.encode("utf-16")).digest())
    return hashed_password


async def start_client_handler(config: str):
    # TODO GraphQL subscriptions are not supported on the HTTP transport.
    #  For subscriptions you should use the websockets transport.
    #  https://gql.readthedocs.io/en/latest/transports/aiohttp.html
    # transport = AIOHTTPTransport(url=api_endpoint, headers={'Authorization': 'token'})
    """
    headers={'Authorization': 'token'} ?
    Alternative:  cookies={"cookie1": "val1"}
    Alternative: Cookie Jar
    jar = aiohttp.CookieJar()
    transport = AIOHTTPTransport(url=url, client_session_args={'cookie_jar': jar})
    """
    api_endpoint = load_gql_api_endpoint(config)
    transport = AIOHTTPTransport(url=api_endpoint, headers={'Authorization': 'token'})
    # Password is default admin base64 password hash from BCO doc:
    # https://basecubeone.org/developer/addon/bco-api-graphql.html#supported-headers
    login_query = parse_graphql_file(LOGIN_QUERY_FILE)
    try:
        client = Client(transport=transport, fetch_schema_from_transport=True)
        auth_token = str(await client.execute_async(login_query))
        logging.info(f"Token for authentication retrieved: {auth_token}")
        transport = AIOHTTPTransport(url=api_endpoint, headers={'Authorization': auth_token})
    except (aiohttp.ClientError, aiohttp.ClientConnectionError) as err:
        logging.error(f"Could not connect to client with api endpoint: {api_endpoint}.\n")
        exit(1)

    # Using `async with` on the client will start a connection on the transport
    # and provide a `session` variable to execute queries on this connection
    async with Client(
            transport=transport,
            fetch_schema_from_transport=True
    ) as session:
        # result = send_graphql_request(session, "")
        # result = await send_graphql_request_file(session, LOGIN_QUERY_FILE)
        # TODO upload files possible?
        # https://levelup.gitconnected.com/how-to-add-file-upload-to-your-graphql-api-34d51e341f38
        client_handler = GraphQLClientHandler(session)
        logging.info(f"Starting authenticated session...")

        get_lights_query = parse_graphql_file(GET_LIGHTS_QUERY_FILE)
        switch_light_mutation = parse_graphql_file(SWITCH_LIGHT_MUTATION_FILE)
        # request = await session.execute(get_lights_query)
        # request = await client_handler.receive_requests(get_lights_query)
        # unit_id_base64_str = "89783086-0f7e-476e-816d-417f24dc7896"
        # unit_id_base64_bytes = unit_id_base64_str.encode('ascii')
        # unit_id_bytes = base64.b64decode(unit_id_base64_bytes)
        # unit_id = unit_id_bytes.decode('ascii')
        unit_id = "89783086-0f7e-476e-816d-417f24dc7896"
        state = "ON"
        request = await client_handler.receive_requests(switch_light_mutation, {"unitId": unit_id, "state": state})
        # response = await client_handler.send_graphql_request(request)
        logging.info(request)


async def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-v', '--verbose', help='', action='store_true')
    parser.add_argument('-d', '--debug', help='', action='store_true')
    parser.add_argument('-c', '--config', help='', nargs=1)
    args = parser.parse_args()

    level = logging.DEBUG if hasattr(args, 'debug') else logging.INFO
    requests_logger.setLevel(logging.WARNING)
    logging.basicConfig(filename='graphql_client.log', level=level)
    # FORMAT = '%(asctime)s %(level)s - %(message)s'
    # logging.basicConfig(format=FORMAT, encoding='utf-8', level=level)
    config = args.config
    await start_client_handler(config)

asyncio.run(main())