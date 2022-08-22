###################################################################################################
#
# sql00.py
# Sqlalchemy database implementation for the ship grid.
#
# Arnoldas Cvirka 2022 August 4th
#
###################################################################################################
# Import libarries
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///grid.db")
Base = declarative_base()

#########################


class Grid(Base):
    __tablename__ = "Grid"
    id = Column(Integer, primary_key=True)
    column = Column("column", Integer)
    row = Column("row", Integer)

    def __init__(self, column, row):
        self.column = column
        self.row = row

    def __repr__(self):
        return f"{self.id}: {self.column}, {self.row}."


Base.metadata.create_all(engine)
