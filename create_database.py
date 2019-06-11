#!/usr/bin/env python
import pymysql


def ceartTable(cursor):
    cursor.execute("drop database if exists todo_db")
    cursor.execute("create database todo_db")
    cursor.execute("use todo_db")

    sql = """create table todo (
    `id` int not null,
    `deadline` varchar(50) not null,
    `title` varchar(50) not null,
    `memo` varchar(50) not null,
    primary key (`id`)
) engine=innodb default charset=UTF8MB4;"""

    cursor.execute(sql)
    print("successfully create table")


if __name__ == '__main__':

    db = pymysql.connect("localhost", "todotest", "todotest", charset="utf8")
    cursor = db.cursor()
    ceartTable(cursor)
    db.commit()
    cursor.close()
    db.close()
