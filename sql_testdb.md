# 命令提示符中操作
    用管理员权限打开命令提示符
    mysql -u root -p

---
```
Microsoft Windows [版本 10.0.18362.836]
(c) 2019 Microsoft Corporation。保留所有权利。

C:\WINDOWS\system32>mysql -u root -p
Enter password: *****
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.7.30-log MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

C:\WINDOWS\system32>mysql -u root -p
Enter password: *****
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 4
Server version: 5.7.30-log MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
```

## show databses; 查看当前所有数据库

---
```
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)
```

## create database testdb; 创建数据库testdb

mysql> create database testdb;
Query OK, 1 row affected (0.00 sec)

## 创建完成后show databases; 显示所有数据库
```
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| testdb             |
+--------------------+
5 rows in set (0.00 sec)
```

## use testdb; 打开指定数据库testdb
```
mysql> use testdb;
Database changed
```

## show tables; 查看当前库的所有表
    show tables from 库名; #查看其他库的表，不切换当前目录
```
mysql> show tables;
Empty set (0.00 sec)

## create table student(); 创建表格student，设置id name sex degree四列以及数据类型
mysql> create table student(
    -> id int(4) not null primary key auto_increment,
    -> name char(20) not null,
    -> sex int(4) not null default '0',
    -> degree double(16,2));
Query OK, 0 rows affected (0.28 sec)
```

## 重新显示表格
```
mysql> show tables;
+------------------+
| Tables_in_testdb |
+------------------+
| student          |
+------------------+
1 row in set (0.00 sec)
```

## desc 表名字; 查看表结构
```
mysql> desc student;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int(4)       | NO   | PRI | NULL    | auto_increment |
| name   | char(20)     | NO   |     | NULL    |                |
| sex    | int(4)       | NO   |     | 0       |                |
| degree | double(16,2) | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
4 rows in set (0.01 sec)
```

## insert into student values(); 插入行，行内信息
```
mysql> insert into student values(1,'jordan',0,89.2);
Query OK, 1 row affected (0.03 sec)

mysql> insert into student values(2,'koopa',0,100.0);
Query OK, 1 row affected (0.11 sec)

mysql> insert into student values(3,'toto',0,62.5);
Query OK, 1 row affected (0.06 sec)
```

## desc 表名字; 查看表结构
```
mysql> desc student;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int(4)       | NO   | PRI | NULL    | auto_increment |
| name   | char(20)     | NO   |     | NULL    |                |
| sex    | int(4)       | NO   |     | 0       |                |
| degree | double(16,2) | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```

## select id,name,sex,degree; 检索id,name,sex,degree列
```
mysql> select id,name,sex,degree;
```
```
ERROR 1054 (42S22): Unknown column 'id' in 'field list'
mysql> select id,name,sex,degree from student;
+----+--------+-----+--------+
| id | name   | sex | degree |
+----+--------+-----+--------+
|  1 | jordan |   0 |  89.20 |  
|  2 | koopa  |   0 | 100.00 |
|  3 | toto   |   0 |  62.50 |
+----+--------+-----+--------+
3 rows in set (0.00 sec)
```
## 导出
```
mysql> mysqldump -u root -p testdb > testtablestudent.sql;
```
/*导出操作，这里需在终端输入，不能在命令提示符输入*/

## desc 表名字; 查看表结构
```
mysql> desc student;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int(4)       | NO   | PRI | NULL    | auto_increment |
| name   | char(20)     | NO   |     | NULL    |                |
| sex    | int(4)       | NO   |     | 0       |                |
| degree | double(16,2) | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```

## exit 退出mysql，不结束服务
```
mysql> exit
Bye
```