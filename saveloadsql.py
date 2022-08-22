###################################################################################################
#
# sql00.py
# Sqlalchemy database implementation for the saving and loading.
#
# Arnoldas Cvirka 2022 August 4th
#
###################################################################################################
# Import libarries
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///space.db")
Base = declarative_base()

#########################


class Space(Base):
    __tablename__ = "Space"
    id = Column(Integer, primary_key=True)
    ship = Column("Ship", String)
    petroleum = Column("Petroleum", Integer)
    currency = Column("Currency", Integer)
    dock = Column("Dock", String)

    def __init__(self, ship, petroleum, currency, dock):
        self.ship = ship
        self.petroleum = petroleum
        self.currency = currency
        self.dock = dock

    def __repr__(self):
        return (
            f"{self.id}: {self.ship}, {self.petroleum},  {self.currency}, {self.dock}."
        )


Base.metadata.create_all(engine)
