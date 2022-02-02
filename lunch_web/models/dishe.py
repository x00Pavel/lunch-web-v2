from .meta import Base
from sqlalchemy import Column, Text, Integer, ForeignKey
from lunch_web import log


class Dishe(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True)
    day = Column(Text, nullable=False)
    name = Column(Text, nullable=True)
    price = Column(Integer, nullable=True)
    raw = Column(Text, nullable=True)

    menu_id = Column(Integer, ForeignKey("menus.id", ondelete="CASCADE"),
                     nullable=False)

    def __repr__(self) -> str:
        return f"name: {self.name}\tprice: {self.price}\tmenu{self.menu_id}"

    
    @staticmethod
    def add_item(session, day, item, menu):
        log.info(f"New dish is added: {item}")
        d = Dishe(name=item["name"], price=item["price"], menu=menu, day=day)
        session.add(d)