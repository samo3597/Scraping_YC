from pydantic import BaseModel

class ITEM(BaseModel):
    id: int
    name: str
    photo: str
    price: float
    discountedPrice: float
    isKilogram: bool
    weightMeasure: str|None
    weightProductPricePerUnit:int|None
    isOnline: bool = True
    categoryId: int = None


class CATEGORY(BaseModel):
    list: list[ITEM]
    pageCount: int
    itemCount: int


class API_CATEGORY(BaseModel):
    success: bool
    data: CATEGORY

class API_ITEM(BaseModel):
    success: bool
    data: ITEM