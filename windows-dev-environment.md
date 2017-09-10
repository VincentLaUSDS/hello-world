# Windows Dev Environment Setup

## Python
I use Anaconda

## R
You can also use Conda to manage R installation.

Note that one error I got using Bash on Ubuntu on windows is install R packages:

```
sh: 1: make: not found
```

Can solve this by https://stackoverflow.com/questions/22784182/r-package-installation-in-linux
```
sudo apt-get install build-essential
```


## Postgresql
https://medium.com/@colinrubbert/installing-ruby-on-rails-in-windows-10-w-bash-postgresql-e48e55954fbf
Lets download and install the latest stable version of PostgreSQL Windows binary.
PostgreSQL 9.6.2 provided by BigSQL: http://oscg-downloads.s3.amazonaws.com/packages/PostgreSQL-9.6.2-2-win64-bigsql.exe 

```
psql -p 5432 -h localhost -U postgres
```

For setting up initial role: https://stackoverflow.com/questions/15301826/psql-fatal-role-postgres-does-not-exist

Connecting to DB (with Azure Postgres): https://stackoverflow.com/questions/44691572/cant-figure-out-db-uri-postgres-azure/44718509?noredirect=1#comment76611471_44718509
