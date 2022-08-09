###################################################################################################
#
# sql00.py
# Sqlalchemy database implementation.
#
# Arnoldas Cvirka 2022 August 4th
#
###################################################################################################
# Import libarries
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///train.db")
Base = declarative_base()

#########################


class Train(Base):
    __tablename__ = "Train"
    id = Column(Integer, primary_key=True)
    petroleum = Column("Petroleum", Integer)
    melonium = Column("Melonium", Integer)
    perks = Column("Perks", String)
    currency = Column("Currency", Integer)
    dock = Column("Dock", String)

    def __init__(self, petroleum, melonium, perks, currency, dock):
        self.petroleum = petroleum
        self.melonium = melonium
        self.perks = perks
        self.currency = currency
        self.dock = dock

    def __repr__(self):
        return f"{self.id}: {self.petroleum}, {self.melonium}, {self.perks}, {self.currency}, {self.dock}."


Base.metadata.create_all(engine)
