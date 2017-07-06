Schema Dump
```
pg_dump $DBURI -s > schema.sql
```

Alternatively,
```
pg_dump -d postgres --host=hostname --username=username --port=5432 -s > schema.sql
```

Load to DB
```
psql $DBURI < schema.sql
```
