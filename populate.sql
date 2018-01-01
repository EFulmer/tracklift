insert into workouts (day) values
(timestamp '2017-10-23');

insert into lifts (workout, warm_up, name, lift_ord) values
(1, false, 'Barbell Overhead Press', 1);

insert into sets (lift, set_ord, set_count, rep_count, warm_up, weight) values
(1, 1, 1, 10, true, 45);

insert into sets (lift, set_ord, set_count, rep_count, warm_up, weight) values
(1, 2, 1, 5, false, 65);

insert into sets (lift, set_ord, set_count, rep_count, warm_up, weight) values
(1, 3, 1, 3, false, 80);


insert into sets (lift, set_ord, set_count, rep_count, warm_up, weight) values
(1, 4, 3, 6, false, 95);
