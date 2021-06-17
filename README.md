# SqlAlchemyTutorial
Repo for Sql Alchemy tutorial 

## Pointers
* SqlAlchemy is a wrapper or ORM(Object relation Mapper) tool kit for python.
* First step of SqlAlchemy: Creating `Engine`
* `Engine` uses `Pool` and `Dialect` to interpret DBAPI.
* We can provide url to `Engine`: Engine derives information about dialect, db specific info, etc.
* We can supply DBAPI connection to `Engine`, We supply the function returning DBAPI connection via `creator` argument of `create_engine` function.
* Example: `create_engine(url, creator=connection_function)`
* To get info about already existing database objects, we need to use reflection.
* Easy approach to load a table from DB `Table(table_name_in_db, metadata, autoload_with=engine)`
