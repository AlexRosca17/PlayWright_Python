from pydantic import BaseModel

from api.response.isbn import Isbn


class BooksAddSuccess(BaseModel):
    books: list[Isbn]