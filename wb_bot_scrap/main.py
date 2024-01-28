import re
import requests
from fake_useragent import UserAgent
from models import Items

ua = UserAgent()
headers = {"user-agent": ua.random}
class ParseWB:
    def __init__(self, url: str):
        self.seller_id = self.get_seller_id(url)

    @staticmethod
    def __get_item_id(url: str):
        regex = "(?<=catalog/).+(?=/detail)"
        item_id = re.search(regex, url)[0]
        return item_id

    def get_seller_id(self, url):
        response = requests.get(url=f"https://card.wb.ru/cards/detail?nm={self.__get_item_id(url=url)}", headers=headers)
        items_info = Items.model_validate(response.json()["data"])
        id = items_info.products[0].id
        name = items_info.products[0].name
        rating = items_info.products[0].reviewRating
        price = items_info.products[0].salePriceU
        data_item = {
            "id": id,
            "name": name,
            "rating": rating,
            "price": price,
            "photo": self.__get_images(items_info)
        
        }
        return data_item
    
    @staticmethod
    def __get_images(item_model: Items):
        for product in item_model.products:
            _short_id = product.id // 100000
            if 0 <= _short_id <= 143:
                basket = '01'
            elif 144 <= _short_id <= 287:
                basket = '02'
            elif 288 <= _short_id <= 431:
                basket = '03'
            elif 432 <= _short_id <= 719:
                basket = '04'
            elif 720 <= _short_id <= 1007:
                basket = '05'
            elif 1008 <= _short_id <= 1061:
                basket = '06'
            elif 1062 <= _short_id <= 1115:
                basket = '07'
            elif 1116 <= _short_id <= 1169:
                basket = '08'
            elif 1170 <= _short_id <= 1313:
                basket = '09'
            elif 1314 <= _short_id <= 1601:
                basket = '10'
            elif 1602 <= _short_id <= 1655:
                basket = '11'
            elif 1656 <= _short_id <= 1919:
                basket = '12'
            else:
                basket = '13'

            link_str = "".join([
                f"https://basket-{basket}.wb.ru/vol{_short_id}/part{product.id // 1000}/{product.id}/images/big/1.jpg"])
            product.image_links = link_str
            return product.image_links

# if __name__ == "__main__":
#     ParseWB("https://www.wildberries.ru/catalog/196252314/detail.aspx?targetUrl=SG")

