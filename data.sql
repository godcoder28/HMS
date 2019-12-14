create schema if not exists coder01 collate utf8mb4_0900_ai_ci;

create table if not exists bookings
(
	bookingid int auto_increment
		primary key,
	name varchar(20) null,
	email varchar(100) not null,
	roomno int null,
	cin date null,
	cout date null
);

create table if not exists rooms
(
	roomn int not null
		primary key,
	status tinyint(1) default 0 null,
	type varchar(20) null
);

