from pydantic import BaseModel, PositiveInt


class ShemaService(BaseModel):
    name: str
    duration: PositiveInt
