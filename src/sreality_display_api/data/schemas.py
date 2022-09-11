from pydantic import BaseModel


class ScrappedFlat(BaseModel):
    id: int
    title: str
    image_url: str

    class Config:
        orm_mode = True