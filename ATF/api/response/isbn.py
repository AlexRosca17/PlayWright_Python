from pydantic import BaseModel


class Isbn(BaseModel):
    isbn: str