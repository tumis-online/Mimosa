from pydantic import BaseModel


class User(BaseModel):
    """User to be created to provide individual application possibilities."""
    first_name: str
    last_name: str

    class Settings(BaseModel):
        pass
