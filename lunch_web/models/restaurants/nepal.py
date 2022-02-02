from lunch_web.models.restaurants.base import BaseRestaurant
import re


class Nepal(BaseRestaurant):

    def __init__(self) -> None:
        self.url = "https://nepalbrno.cz/weekly-menu/"
        self.short_name = "nepal"
        self.full_name = "Nepal"

    def parse_page(self):
        result = dict()
        table = self.page.find("div", class_="the_content_wrapper").find_all("table")[2]
        rows = table.find_all("tr")
        day_stack = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "end"]

        week_day = None
        for row in rows:
            for column in row.find_all("td"):
                day = day_stack[0]
                column_text = column.get_text().strip()
                if day in column_text:
                    week_day = column_text
                    result[week_day] = list()
                    day_stack.pop(0)
                elif "" != column_text:
                    sibling = column.find_next_siblings()[0]
                    price = self.get_price_from_string(sibling.get_text())
                    result[week_day].append(
                        {"type": None, "name": column_text, "price": price})
                    break
        return result
