from pydantic import BaseModel

class ITEM(BaseModel):
    id: int
    name: str
    photo: str
    price: float
    discountedPrice: float
    isKilogram: bool
    weightMeasure: str
    weightProductPricePerUnit:int


class CATEGORY(BaseModel):
    list: list[ITEM]
    pageCount: int
    itemCount: int


class API_CATEGORY(BaseModel):
    success: bool
    data: CATEGORY
