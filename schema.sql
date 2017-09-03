drop table if exists lifts;
create table if not exists lifts (
    id serial primary key
    , name text not null
    , day date not null
    , sets int not null
    , reps int not null
    , notes text not null
    , set_ord int not null
    , day_ord int not null
)
