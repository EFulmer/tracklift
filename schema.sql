drop table if exists workouts cascade;
create table if not exists workouts (
    id serial primary key
    , day date not null
);

drop table if exists lifts cascade;
create table if not exists lifts (
    id serial primary key
    , workout serial references workouts(id)
    , warm_up boolean not null
    , name text not null
    , lift_ord int not null
);

drop table if exists sets cascade;
create table if not exists sets (
    id serial primary key
    , lift serial references lifts(id)
    , set_ord int not null
    , set_count int not null
    , rep_count int not null
    , weight int not null
    , warm_up boolean not null
    , notes text
);
