from pydantic import BaseModel

class MenuList(BaseModel):
    id: int
    name: str
    category: str
    available: bool


class MenuResponse(BaseModel):
    status: str="success"
    count: int
    lists: list[MenuList]