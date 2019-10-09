# About
Mini module to work with PostgreSQL

# Install

Use pip:
```
pip install postgresql-mini-connector
```

# Usage

Add this module in your project and start using

```
from postgresqlconnector import DB
print(DB.query('''select * from pg_stat_activity'''))
```
