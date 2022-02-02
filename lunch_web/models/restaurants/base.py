import requests
from bs4 import BeautifulSoup
import re
from lunch_web import log

class BaseRestaurant:
    url: str = None
    short_name: str = None
    full_name: str = None
    encoding: str = "utf-8"
    page = None

    def get_html(self):
        respons = requests.get(self.url)
        content = respons.text
        self.page = BeautifulSoup(content, "html.parser")

    def get_menu(self):
        self.get_html()
        dishes = self.parse_page()
        result = {"restaurant": self.full_name, "dishes": dishes}
        return result

    def parse_page(self): ...

    def get_price_from_string(self, price):
        log.info(f"Price string: {price}")

        if re.match("\([0-9, ]+\)", price):
            return 0
        price = re.sub("\D", "", price)
        if price == "":
            return 0
            
        return int(price)