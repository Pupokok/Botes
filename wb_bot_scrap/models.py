from pydantic import BaseModel, root_validator

class Item(BaseModel):
    id: int
    name: str
    salePriceU: int
    reviewRating: float
    pics: int
    image_links: str = None
    
    @root_validator(pre=True)
    def conver_sale_price(cls, values: dict):
        sale_price = values.get("salePriceU")
        if sale_price is not None:
            values["salePriceU"] = sale_price / 100
        return values
    
class Items(BaseModel):
    products: list[Item]