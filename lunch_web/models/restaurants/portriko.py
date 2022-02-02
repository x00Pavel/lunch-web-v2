from lunch_web.models.restaurants.base import BaseRestaurant
from lunch_web import log
import re

class Portoriko(BaseRestaurant):

    def __init__(self) -> None:
        self.url = "https://restauraceportoriko.cz/denni-menu/"
        self.short_name = "portoriko"
        self.full_name = "Restaurace Portoriko"
        self.page = None

    def parse_page(self):
        result = dict()
        div = self.page.find("div", class_="print-not")
        for n in div.find_all("h2"):
            day = n.get_text()
            result[day] = list()
            table = n.find_next_siblings()[0]
            for x in table.find_all("td", class_="middle-menu"):
                if len(x.get_text(strip=True)) != 0:
                    txt = x.get_text()
                    price =  self.get_price_from_string(txt.split()[-1])
                    result[day].append(
                        {"name": " ".join(txt.split()[0:-1:1]),
                        "price": price})
        return result
