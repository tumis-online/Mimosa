"""Constants for GraphQL Client Request Files."""


class RequestFile:
    """Stores GQL request file constants."""

    class Query:
        """Query Requests to get info about items."""
        QUERY_BASE = "requests/queries/"
        LOGIN = QUERY_BASE + "login.graphql"
        GET_LIGHTS = QUERY_BASE + "get_lights.graphql"
        GET_COLORABLE_LIGHTS = QUERY_BASE + "get_colorable_lights.graphql"
        GET_DEVICES = QUERY_BASE + "get_devices.graphql"
        GET_LOCATIONS = QUERY_BASE + "get_locations.graphql"

    class Mutation:
        """Mutation Requests for changing (adding, removing...) items."""
        MUTATION_BASE = "requests/mutations/"

        # Light mutations
        SWITCH_LIGHT = MUTATION_BASE + "switch_light.graphql"
        CHANGE_COLOR = MUTATION_BASE + "change_color.graphql"
        DIM_LIGHT = MUTATION_BASE + "dim_light.graphql"

        # General item mutations
        ADD_ITEM = MUTATION_BASE + "add_item.graphql"
        REMOVE_ITEM = MUTATION_BASE + "remove_item.graphql"
        ADD_SCENE = MUTATION_BASE + "add_scene.graphql"
        REMOVE_SCENE = MUTATION_BASE + "remove_scene.graphql"

    class Subscription:
        """Subscription Requests for instant actualization."""
