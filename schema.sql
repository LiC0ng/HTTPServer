-- schema.sql

drop database if exists todo_db;

create database todo_db;

use todo_db;

create table todo (
    `id` int not null,
    `deadline` varchar(50) not null,
    `title` varchar(50) not null,
    `memo` varchar(50) not null,
    primary key (`id`)
) engine=innodb default charset=utf8;