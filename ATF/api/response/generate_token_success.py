from pydantic import BaseModel


class GenerateTokenSuccessResponse(BaseModel):
    token: str | None
    expires: str | None
    status: str
    result: str