create database 2608012360_verk7;

CREATE TABLE 2608012360_verk7.users(
	user varchar(32) not null,
    pass varchar(32) not null,
    nafn varchar(32) not null,
    PRIMARY KEY (user)
);
insert into 2608012360_verk7.users(user,pass,nafn) value ('2608012360','123456','Sunna')