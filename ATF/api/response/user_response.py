from pydantic import BaseModel


class UserResponse(BaseModel):

    userID: str
    username: str
    books: list[dict[str, str]]
    