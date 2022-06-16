import asyncio

import aiofiles as aiofiles
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


async def main():
    host = "localhost"
    port = 13781
    suffix = "/graphql"
    api_endpoint = "http://" + host + ":" + str(port) + suffix
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
        # Execute single query
        query = gql(
            """
            query getContinents {
              continents {
                code
                name
              }
            }
            """
        )

        '''
            File upload list
        '''
        query = gql('''
          mutation($files: [Upload!]!) {
            multipleUpload(files: $files) {
              id
            }
          }
        ''')

        file_path_1 = "YOUR_FILE_PATH_1"
        file_path_2 = "YOUR_FILE_PATH_2"
        f1 = open(file_path_1, "rb")
        f2 = open(file_path_2, "rb")

        params = {"files": [f1, f2]}

        '''
            Alternatively, streaming files
        '''

        async def file_sender(file_name):
            async with aiofiles.open(file_name, 'rb') as f:
                chunk = await f.read(64 * 1024)
                while chunk:
                    yield chunk
                    chunk = await f.read(64 * 1024)

        params = {"file": file_sender(file_name='YOUR_FILE_PATH')}

        result = await session.execute(
            query, variable_values=params, upload_files=True
        )

        f1.close()
        f2.close()

        result = await session.execute(query)
        print(result)


asyncio.run(main())
