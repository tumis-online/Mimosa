"""Test module for GraphQL Client."""
from bco.api.graphql.client import start_client


# content of test_class.py
class TestGraphQLClient:

    default_config = {
            "host": "localhost",
            "port": 13781,
            "suffix": "/graphql"
        }

    api_endpoint_url = f"http://{default_config['host']}:{str(default_config['port'])}{default_config['suffix']}"

    def test_no_config_file(self) -> None:
        """Default config could be transport url from GraphQL Playground https://countries.trevorblades.com/"""
        assert setup.load_gql_api_endpoint() == self.api_endpoint_url

    def test_incorrect_config(self) -> None:
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
