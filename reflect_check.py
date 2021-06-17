from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine("sqlite:///orm-test.db")
metadata = MetaData(engine)

table = Table("User", metadata, autoload_with=engine)  # for reading existing table in DB

for col in table.columns:
    print(col.type.__str__())

if __name__ == '__main__':
    with engine.begin() as connection:
        print(connection.execute(select(table)).fetchall())

