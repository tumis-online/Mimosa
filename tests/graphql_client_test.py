"""Test module for GraphQL Client."""
from GraphQL_client import graphql_client


default_config = {
        "host": "localhost",
        "port": 13781,
        "suffix": "/graphql"
    }

api_endpoint_url = f"http://{default_config['host']}:{str(default_config['port'])}{default_config['suffix']}"


def test_no_config_file() -> None:
    """Default config could be transport url from GraphQL Playground https://countries.trevorblades.com/"""
    assert graphql_client.load_gql_api_endpoint(None) == api_endpoint_url


def test_incorrect_config_file() -> None:
    pass


def test_valid_config_file() -> None:
    pass


def test_invalid_query() -> None:
    pass


def test_valid_query() -> None:
    pass


def test_valid_mutation() -> None:
    pass


def test_send_invalid_file() -> None:
    pass


def test_send_valid_file() -> None:
    pass


def test_send_multiple_files() -> None:
    pass


def test_stream_request_file() -> None:
    pass


