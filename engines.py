from sqlalchemy import create_engine, text


engine = create_engine("sqlite:///:memory:")  # engine for info about data bases and connectors(dbapi)
connection = engine.connect()  # creating connection, can be used with context manager.
# SQL Alchemy provides us API for smooth transactions

# creating table
create_table = text("CREATE TABLE some_table (x int, y int)")
connection.execute(create_table)

# inserting data
connection.execute(
    text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
    [{"x": 1, "y": 3}, {"x": 2, "y": 4}]
)

# fetchall -> list of tuple, fetchone -> tuple
result = connection.execute(text("select * from some_table"))
# commit is not relevant in the context of in memory

if __name__ == '__main__':
    print(result.fetchone()[1])
