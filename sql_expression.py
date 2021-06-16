from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine, and_, or_, select
from sqlalchemy.dialects import mysql, postgresql

metadata = MetaData()

# defining table
user_table = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255))
)

engine = create_engine("sqlite:///:memory:")

# creating sql expression(it won't return boolean), i will be used in sql
expression = or_(and_(user_table.c.id > 6,
                      user_table.c.id < 10),
                 user_table.c.name == "Arnab")

insert_statement = user_table.insert().values(
    id=23,
    name="Arnab"
)

with engine.begin() as conn:
    metadata.create_all(conn)
    conn.execute(insert_statement)

    # multi row insert
    conn.execute(user_table.insert(),
                 [
                     {"id": 56, "name": "gogo"},
                     {"id": 89, "name": "pogo"}
                 ]
                 )
    print(conn.execute(select(user_table)).fetchall())
    print(conn
          .execute(
                select(user_table)
                .where(expression)  # select with where clause
            ).fetchall()
          )

if __name__ == '__main__':
    # making expressions sql agnostic
    print(f"raw expression: {expression}")
    print(f"raw expression: {expression.compile(dialect=mysql.dialect())}")
    print(f"raw expression: {expression.compile(dialect=postgresql.dialect())}")
