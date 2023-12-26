from pydantic import BaseModel, ConfigDict, PositiveInt


class ShemaService(BaseModel):
    name: str
    duration: PositiveInt


class CreateService(ShemaService):
    pass


class GetService(ShemaService):
    model_config = ConfigDict(from_attributes=True)
    id: int
