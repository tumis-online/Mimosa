import asyncio
import json
import logging
import os.path

import aiofiles

from gql import gql, Client

GQL_SINGLE_FILE_UPLOAD_MUTATION = '''
      mutation($file: Upload!) {
        singleUpload(file: $file) {
          id
        }
      }
    '''
GQL_MULTIPLE_FILE_UPLOAD_MUTATION = '''
      mutation($files: [Upload!]!) {
        multipleUpload(files: $files) {
          id
        }
      }
    '''
MAX_LOCAL_FILE_SIZE = 300


def parse_graphql_file(request_file):
    """Parse to get string of graphql file.
    :return: string of GraphQL file
    """
    with open(request_file, 'r') as request:
        query_str = request.read()
    query = gql(query_str)
    return query


async def execute_query(session: Client, query) -> json:
    """Execute query via gql.
    :param session gql client
    :param query
    """
    result = session.execute(query)
    return result


async def execute_subscription(session: Client, subscription) -> json:
    """Execute subscription via gql.
    :param session gql client
    :param subscription
    """
    result = session.subscribe(subscription)
    return result


class GraphQLClientHandler:
    """Handles GQL Client async session for sending requests to API."""
    session: Client
    current_request: str = None

    def __init__(self, session):
        self.loop = asyncio.get_event_loop()
        self.session = session

    async def execute_query(self, query, params=None):
        """Executing GraphQL query asynchronously."""
        # file_upload = False if params is None else True
        file_upload = False
        result = self.session.execute(query, variable_values=params, upload_files=file_upload)
        return result

    async def send_graphql_request(self, graphql_request, params=None):
        """Executing a single query.
        :return result of GraphQL request
        """
        result = await self.execute_query(graphql_request, params)
        return result

    async def send_multiple_graphql_request_files(self, graphql_files: list):
        """Send multiple query files.
        :return result of GraphQL request
        """
        logging.info("Send multiple GraphQL requests from multiple files: %s.", graphql_files)
        query = gql(GQL_MULTIPLE_FILE_UPLOAD_MUTATION)
        files: list = []
        for f_path in graphql_files:
            file = open(f_path, "rb")
            files.append(file)

        params = {"files": graphql_files}

        result = await self.execute_query(query, params)

        for file in files:
            file.close()
        return result

    async def send_graphql_request_file(self, graphql_file):
        """Send a query file.
        :return result of GraphQL request
        """
        logging.info("Sending GraphQL request from file: %s.", graphql_file)
        file_size = os.path.getsize(graphql_file)
        if file_size > MAX_LOCAL_FILE_SIZE:
            return await self.stream_graphql_request_file(graphql_file)
        query = gql(GQL_SINGLE_FILE_UPLOAD_MUTATION)

        with open(graphql_file, "rb") as file:
            params = {"file": file}

            result = await self.execute_query(query, params)
        return result

    async def stream_graphql_request_file(self, graphql_file: str):
        """Use streaming for big file to limit amount of memory used.
        :return result of GraphQL request
        """
        logging.info("Streaming GraphQL request from file: %s.", graphql_file)
        query = gql(GQL_MULTIPLE_FILE_UPLOAD_MUTATION)

        async def file_sender(file_name):
            async with aiofiles.open(file_name, 'rb') as file:
                chunk = await file.read(64 * 1024)
                while chunk:
                    yield chunk
                    chunk = await file.read(64 * 1024)

        params = {"file": file_sender(file_name=graphql_file)}

        result = await self.execute_query(query, params)
        return result
