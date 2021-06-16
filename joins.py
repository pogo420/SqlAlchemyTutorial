from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine, select


metadata = MetaData()

# defining table
user_table = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255))
)

user_email_table = Table(
    "user_email",
    metadata,
    Column("id", Integer),
    Column("email", String(255))
)

engine = create_engine("sqlite:///:memory:")

with engine.begin() as conn:
    metadata.create_all(conn)

    # insert user
    conn.execute(user_table.insert(),
                 [
                     {"id": 90, "name": "ola"},
                     {"id": 56, "name": "gogo"},
                     {"id": 89, "name": "pogo"}
                 ]
                 )

    conn.execute(user_email_table.insert(),
                 [
                     {"id": 90, "email": "ola@gmail.com"},
                     {"id": 56, "email": "gogo@yahoo.com"},
                     {"id": 89, "email": "pogo@hotmail.com"}
                 ]
                 )

    print(conn.execute(select(user_table)).fetchall())
    print(conn.execute(select(user_email_table)).fetchall())

    # join example
    print(conn.execute(
            select(user_email_table.join(user_table, user_email_table.c.id == user_table.c.id))
        ).fetchall()
    )

if __name__ == '__main__':
    pass
