from datetime import timedelta
from operator import and_

from .meta import Base
from .dishe import Dishe
from sqlalchemy import Column, Text, Integer, Date, and_
from sqlalchemy.orm import relationship
from lunch_web import log
from lunch_web.models import restaurants

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True)
    start = Column(Date, nullable=False)
    end = Column(Date, nullable=False)
    restaurant_name = Column(Text, nullable=False)

    dishe_list = relationship("Dishe", 
        backref="menu",
        cascade="all, delete",
        passive_deletes=True)
    
    def __repr__(self) -> str:
        return f"{self.id}: menu {self.restaurant_name} from "\
               f"{self.start} until {self.end} dishes: {self.dishe_list}"

    @staticmethod
    def get_current_menus(session, date):
        query = session.query(Menu) \
            .filter(and_(date <= Menu.end, date >= Menu.start))
        log.info(query)
        return query.all()

    @staticmethod
    def update_menus(session, date):
        menus = restaurants.get_sources()
        start = date - timedelta(days=(6 - date.weekday()))
        end = start + timedelta(days=6)

        for entry in menus:
            log.debug(entry)
            menu = Menu(start=start, end=end,
                        restaurant_name=entry["restaurant"])
            session.add(menu)

            log.info(entry["dishes"])

            for day, items in entry["dishes"].items():
                for i in items:
                    log.info(f"Item to be added: {i}")
                    Dishe.add_item(session, day, i, menu)

        return menus
