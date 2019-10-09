# About
Mini module to work with PostgreSQL

# Install

Use pip:
```
pip install postgresql-mini-connector
```

# Simple Start for home project

## Install package from pip
## Use connector
```
from postgresqlconnector import DB
print(DB.query('''select * from pg_stat_activity'''))
```

## API

* query
Get all rows from your sql query
Param:
  * sql: str - Your query
  * params: dict - Params for query 
Result:
  * Array of Record
```
result = DB.query('''select * from pg_stat_activity''')
print(result[0])
print(result[0].pid)
```
* row
Get first row from your sql query
Param:
  * sql: str - Your query
  * params: dict - Params for query 
Result:
  * Record
```
result = DB.query('''select * from pg_stat_activity''')
print(result.pid)
```
* scalar
Get first column from first row from you sql query
Param:
  * sql: str - Your query
  * params: dict - Params for query 
Result:
  * Scalar
```
result = DB.query('''select pid, * from pg_stat_activity''')
print(result)
```
* set_connection_info
Set database connections
Param:
  * host: str = 'localhose' - Host
  * port: str = '5432' - Port
  * dbname: str = 'postgres' - Database name
  * user: str = 'postgres' - User
  * password: str = 'postgres' - Password
