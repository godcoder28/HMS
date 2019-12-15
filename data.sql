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
INSERT INTO coder01.rooms (roomn, status, type) VALUES (101, 0, 'suit');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (102, 0, 'suit');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (103, 0, 'suit');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (104, 0, 'suit');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (105, 0, 'suit');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (201, 0, 'executive');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (202, 0, 'executive');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (203, 0, 'executive');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (204, 0, 'executive');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (205, 0, 'executive');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (301, 0, 'deluxe');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (302, 0, 'deluxe');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (303, 0, 'deluxe');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (304, 0, 'deluxe');
INSERT INTO coder01.rooms (roomn, status, type) VALUES (305, 0, 'deluxe');
