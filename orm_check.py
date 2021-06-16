from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine, and_, or_, select

engine = create_engine("sqlite:///orm-test.db")

Base = declarative_base()
Session = sessionmaker(engine)


class User(Base):
    __tablename__ = "user"

    id_ = Column("id", Integer, primary_key=True)
    name = Column("name", String)

    def __init__(self, id_, name):
        self.name = name
        self.id_ = id_


Base.metadata.create_all(engine)
session = Session()  # act as unit of work, all steps under a session are atomic in nature.

for i in range(50):
    session.add(User(i+1, f"Person{i}"))

# ignoring for now
# session.commit()
# session.close()

if __name__ == '__main__':
    for user in session.query(User).filter(User.id_ > 30).filter(User.id_ < 40):
        print(user.id_, user.name)
