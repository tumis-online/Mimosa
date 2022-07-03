"""Test module for GraphQL Client."""
from bco.api.graphql.client import start_client
from hypothesis import given, example
from hypothesis.strategies import text, data, integers
from typing import Callable


# Testing class for GraphQL client connection handling
class TestGraphQLClient:

    default_config = {
            "host": "localhost",
            "port": 13781,
            "suffix": "/graphql"
        }

    api_endpoint_url = f"http://{default_config['host']}:{str(default_config['port'])}{default_config['suffix']}"

    @given(text())
    @example()
    def test_password_hash(self):
        pass

    def test_no_config_file(self) -> None:
        """Default config could as well be transport url from GraphQL Playground https://countries.trevorblades.com/"""
        assert start_client.load_gql_api_endpoint() == self.api_endpoint_url

    @given(data())
    def test_incorrect_config(self) -> None:
        host: str = data.draw(text())
        port: int = data.draw(integers())
        suffix: str = data.draw(text())
        incorrect_config = {"host": host, "port": port, "suffix": suffix}
        pass

    def test_valid_config(self) -> None:
        pass

    def test_invalid_query(self) -> None:
        pass

    def test_valid_query(self) -> None:
        pass

    def test_valid_mutation(self) -> None:
        pass

    def test_send_invalid_file(self) -> None:
        pass

    def test_send_valid_file(self) -> None:
        pass

    def test_send_multiple_files(self) -> None:
        pass

    def test_stream_request_file(self) -> None:
        pass

    def test_parse_graphql_file(self) -> None:
        pass
