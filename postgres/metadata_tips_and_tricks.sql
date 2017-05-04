/*
This file contains some example sql queries to select certain metadata such as
comments, indices, constraints
*/

--Selecting Constraints
select
  *
from information_schema.table_constraints
where table_name = <table_name>
;

--Selecting Indices
select
    t.oid as oid,
    t.relname as table_name,
    i.relname as index_name,
    a.attname as column_name
from
    pg_class t,
    pg_class i,
    pg_index ix,
    pg_attribute a
where
    t.oid = ix.indrelid
    and i.oid = ix.indexrelid
    and a.attrelid = t.oid
    and a.attnum = ANY(ix.indkey)
    and t.relkind = 'r'
    and t.relname = <table_name>
order by
    t.relname,
    i.relname
;

--Retrieving Comments
select *
from pg_description
  join pg_class
    on pg_description.objoid = pg_class.oid
  join pg_namespace
    on pg_class.relnamespace = pg_namespace.oid
where pg_namespace.nspname = <schema_name>
 and pg_class.relname = <table_name>
;
