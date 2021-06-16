from sqlalchemy import MetaData, Table, Column, Integer, String, select, create_engine

metadata = MetaData()

# defining table
user_table = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255))
)

engine = create_engine("sqlite:///:memory:")

with engine.begin() as conn:
    user_table.create(conn)  # creating table


if __name__ == '__main__':
    print(f"Table name: {user_table.name}, columns: {user_table.c}")
    print(f"select statement {select(user_table)}")  # generating select statement
    print(f"tables associated: {metadata.tables.keys()}")
