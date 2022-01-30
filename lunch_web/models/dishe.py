from .meta import Base
from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Dishe(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True)

    name = Column(Text, nullable=True)
    price = Column(Integer, nullable=True)
    raw = Column(Text, nullable=True)

    menu_id = Column(ForeignKey("menus.id"), nullable=False)

    menu = relationship("Menu", cascade="all, delete")
