/*
This file contains some example sql queries to select certain metadata such as
comments, indices, constraints
*/

--Selecting Constraints
select
  *
from information_schema.table_constraints
where table_schema = <table_schema>
  and table_name = <table_name>
;

--Selecting constraints along with check clauses
select
  tc.*,
  cc.check_clause
from information_schema.table_constraints as tc
  left join information_schema.check_constraints as cc
    on tc.constraint_schema = cc.constraint_schema
      and tc.constraint_name = cc.constraint_name
;

--Selecting Keys (Both unique and primary)
select
  kcu.table_schema,
  kcu.table_name,
  kcu.constraint_name,
  tc.constraint_type,
  kcu.column_name,
  kcu.ordinal_position,
  kcu.position_in_unique_constraint
from information_schema.key_column_usage as kcu
left join information_schema.table_constraints as tc
  on kcu.table_schema = tc.table_schema
    and kcu.table_name = tc.table_name
    and kcu.constraint_name = tc.constraint_name
;

--Selecting Indices
select
  t.oid as oid,
  ns.nspname as table_schema,
  t.relname as table_name,
  i.relname as index_name,
  a.attname as column_name
from pg_class as t
  join pg_index as ix
    on t.oid = ix.indrelid
  join pg_class as i
    on i.oid = ix.indexrelid
  join pg_attribute as a
    on a.attrelid = t.oid
      and a.attnum = any(ix.indkey)
  join pg_namespace as ns
    on t.relnamespace = ns.oid
  and t.relkind = 'r'
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

--Selecting Actively running queries
select 
  pid,
  usename,
  application_name,
  query_start,
  now() - query_start as time_elapsed,
  state,
  query
from pg_stat_activity
where pid <> pg_backend_pid()
order by pid
;
