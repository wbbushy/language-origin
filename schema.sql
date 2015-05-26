drop table if exists entries;
create table languages (
  id integer primary key autoincrement,
  name text not null,
  'text' text not null
);
