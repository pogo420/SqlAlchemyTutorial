from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine, and_, or_, select

engine = create_engine("sqlite:///orm-test.db")

Base = declarative_base()
Session = sessionmaker(engine)


class User(Base):
    __tablename__ = "user"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)


Base.metadata.create_all(engine)
session = Session()

arnab = User()
