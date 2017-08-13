# Schema Dump
```
pg_dump $DBURI -s > schema.sql
```

For example,
```
pg_dump -d postgres --host=hostname --username=username --port=5432 -s > schema.sql
```

After running the above command, it will prompt for a password. Enter the password.

If you run into an error that looks like the following:
```
pg_dump: server version: 9.6.2; pg_dump version: 9.5.7
pg_dump: aborting because of server version mismatch
```

You need to update your version of `pg_dump`. The following is a potential solution: https://github.com/laradock/laradock/issues/778 (Confirmed that this works on Bash on Ubuntu for Windows)

```
sudo apt-get update
sudo apt-get install wget
sudo add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql-client-9.6
pg_dump -V
```

This might not actually update the default version of `pg_dump`. What this does is that it installs the updated version of postgresql (in this case 9.6). So if you look for the versions of `pg_dump` using:

```
(datasci-sba) vla@DESKTOP-5P8QQKP /mnt/c/Users/vla/git/datasci-sba (master) $ find / -name pg_dump -type f 2>/dev/null
/usr/lib/postgresql/9.5/bin/pg_dump
/usr/lib/postgresql/9.6/bin/pg_dump
```

One solutions would be to just point the right version of `pg_dump`, for example

```
/usr/lib/postgresql/9.6/bin/pg_dump -d postgres --host=hostname --username=username --port=5432 -s > schema.sql
```

# Load to DB
```
psql $DBURI < schema.sql
```

For example,
```
psql postgres://localhost:5432/VincentLa < schema.sql
```
