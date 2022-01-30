from .meta import Base
from sqlalchemy import Column, Text, Integer, Date


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True)
    start = Column(Date, nullable=False)
    end = Column(Date, nullable=False)
    restaurant_name = Column(Text, nullable=False)
