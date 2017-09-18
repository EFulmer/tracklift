drop table if exists workouts;
create table if not exists workouts (
    id serial primary key
    , day date not null
);

drop table if exists lifts;
create table if not exists lifts (
    id serial primary key
    , workout serial references workouts(id)
    , warm_up boolean not null
    , name text not null
    , lift_ord int not null
    , workout_ord int not null
);

drop table if exists sets;
create table if not exists sets (
    id serial primary key
    , lift serial references lifts(id)
    , set_count int not null
    , rep_count int not null
    , weight int not null
    , notes text not null
    , lift_ord int not null
);
