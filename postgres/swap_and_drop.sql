-- Example of how to do swap and drop style creation of tables in Postgres
-- Note that even though this is one transaction, by doing swap and drop, users can still query
-- off of test.testing. (you can still query even during the pg sleep). At the very end, the drop
-- and swap happens quickly to reduce chances of locks happening.

begin;

drop table if exists test.testing_swap;
create table test.testing_swap as
(
select 1 as col_name
);

select pg_sleep(15);

drop table if exists test.testing;
alter table if exists test.testing_swap rename to testing;

commit;
