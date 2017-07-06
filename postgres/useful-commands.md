Schema Dump
```
pg_dump $DBURI -s > schema.sql
```

For example,
```
pg_dump -d postgres --host=hostname --username=username --port=5432 -s > schema.sql
```

Load to DB
```
psql $DBURI < schema.sql
```

For example,
```
psql postgres://localhost:5432/VincentLa < schema.sql
```
