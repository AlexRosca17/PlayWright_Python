from pydantic import BaseModel

from api.response.books import BooksStructure


class BooksResponse(BaseModel):
    books: list[BooksStructure]
