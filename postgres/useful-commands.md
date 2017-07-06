Schema Dump
```
pg_dump $DBURI -s > schema.sql
```

Load to DB
```
psql $DBURI < schema.sql
```
