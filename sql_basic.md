[SQL必知必会 第四版](https://weread.qq.com/web/reader/95232130715c01b39521460k8f132430178f14e45fce0f7)
#1.数据库基础
---
## 数据库
数据库软件应称为数据库管理系统（DBMS）
将数据库想象为一个文件柜。这个文件柜是一个存放数据的物理位置，不管数据是什么，也不管数据是如何组织的。

## 表
你往文件柜里放资料时，是在文件柜中创建文件，然后将相关的资料放入特定的文件中。
在数据库领域中，这种文件称为表。表是一种结构化的文件，可用来存储某种特定类型的数据。表可以保存顾客清单、产品目录，或者其他信息清单。
数据库中的每个表都有一个名字来标识自己。这个名字是唯一的，即数据库中没有其他表具有相同的名字。

## 列
正确地将数据分解为多个列极为重要。例如，城市、州、邮政编码应该总是彼此独立的列。
数据库中每个列都有相应的数据类型。数据类型（datatype）定义了列可以存储哪些数据种类。
例如，如果列中存储的是数字（或许是订单中的物品数），则相应的数据类型应该为数值类型。
如果列中存储的是日期、文本、注释、金额等，则应该规定好恰当的数据类型。

## 行
表中的数据是按行存储的，所保存的每个记录存储在自己的行内。如果将表想象为网格，网格中垂直的列为表列，水平行为表行。

## 主键
表中每一行都应该有一列（或几列）可以唯一标识自己。
一列（或一组列），其值能够唯一标识表中每一行。

**注意：**记录一旦插入到表中，主键最好不要再修改，因为主键是用来唯一定位记录的，修改了主键，会造成一系列的影响。
主键不要带有业务含义，而应该使用BIGINT自增或者GUID类型。主键也不应该允许NULL。
可以使用多个列作为联合主键，但联合主键并不常用。
可以使用自增类型：BIGINT NOT NULL AUTO_INCREMENT类型

    全局唯一GUID类型：类似8f55d96b-8acc-4636-8cb8-76bf8abc2f57。
	GUID算法通过网卡MAC地址、时间戳和随机数保证任意计算机在任意时间生成的字符串都是不同的，大部分编程语言都内置了GUID算法，可以自己预算出主键。

## 外键
外键并不是通过列名实现的，而是通过定义外键约束实现的：
一个classes的记录可以对应多个students表的记录。
```
ALTER TABLE students
ADD CONSTRAINT fk_class_id
FOREIGN KEY (class_id)
REFERENCES classes (id);
```

# 2.什么是SQL
---
Structured Query Language（结构化查询语言）

## SELECT语句
检索单个列：

>SELECT 想选择什么
FROM 从什么地方选择;

比如：
```
SELECT prod_id,prod_names,prod_price -- 行内注释
From Products;
```

## 单行注释
/*    多行注释    */

多条SQL语句必须以分号（;）分隔。SQL语句不区分大小写，在处理SQL语句时，其中所有空格都被忽略。
SQL语句一般返回原始的、无格式的数据。数据的格式化是表示问题，而不是检索问题。

## 检索所有列
```
SELECT *
From Products;
```

除非你确实需要表中的每一列，否则最好别使用＊通配符。检索不需要的列通常会降低检索和应用程序的性能。

## 检索不同的值
DISTINCT关键字
```
SELECT DISTINCT vend_id
From Products;
```

SELECT DISTINCT vend_id告诉DBMS只返回不同（具有唯一性）的vend_id行
如果使用DISTINCT关键字，它必须直接放在列名的前面
DISTINCT关键字作用于所有的列，不仅仅是跟在其后的那一列。

## 限制结果
在SQL Server和Access中使用SELECT时，可以使用TOP关键字来限制最多返回多少行，SELECT TOP 5，只检索前5行数据。
```
SELECT TOP 5 prod_names
From Products;
```

如果使用的是DB2
```
SELECT prod_names
From Products
FATCH FIRST 5 ROWS ONLY;
```

如果使用Oracle，需要基于ROWNUM（行计数器）来计算行
```
SELECT prod_names
From Products
WHERE ROWNUM <= 5;
```

如果使用MySQL、MariaDB、PostgreSQL或者SQLite，需要使用LIMIT子句
```
SELECT prod_names
From Products
LIMIT 5 OFFSET 5;
```

LIMIT 5 OFFSET 5指示MySQL等DBMS返回从第5行起的5行数据。第一个数字是检索的行数，第二个数字是指从哪儿开始。
**注意：**第一个被检索的行是第0行，而不是第1行。因此，LIMIT 1 OFFSET 1会检索第2行，而不是第1行。

MySQL、MariaDB和SQLite支持简化版的LIMIT 4 OFFSET 3语句，即LIMIT 3,4。

# 3.排序检索数据
---
## 排序数据
在指定一条ORDER BY子句时，应该保证它是SELECT语句中最后一条子句。
```
SELECT prod_id,prod_names,prod_price
From Products
ORDER BY prod_price,prod_names;
```

先按price排序，之后按names排序。仅在多个行具有相同的prod_price值时才对产品按prod_name进行排序。如果prod_price列中所有的值都是唯一的，则不会按prod_name排序。

## 按列位置排序
**尽量不采用这种方式**

```
SELECT prod_id,prod_names,prod_price
From Products
ORDER BY 2,3;
```

## 指定排序方向
为了进行降序排序，必须指定DESC关键字。
DESC是DESCENDING的缩写，这两个关键字都可以使用。与DESC相对的是ASC（或ASCENDING）

```
SELECT prod_id,prod_names,prod_price
From Products
ORDER BY prod_price DESC,prod_names;
```

DESC关键字只应用到直接位于其前面的列名。因此，prod_price列以降序排序，而prod_name列（在每个价格内）仍然按标准的升序排序。

# 4.过滤数据
---
## 使用WHERE子句
数据库表一般包含大量的数据，很少需要检索表中的所有行。通常只会根据特定操作或报告的需要提取表数据的子集。
只检索所需数据需要指定搜索条件（search criteria），搜索条件也称为过滤条件（filter condition）
在SELECT语句中，数据根据WHERE子句中指定的搜索条件进行过滤。WHERE子句在表名（FROM子句）之后给出。
```
SELECT prod_id,prod_names,prod_price
From Products
WHERE prod_price = 3.49;
```
从products表中检索两个列，只返回prod_price值为3.49的行
应该让ORDER BY位于WHERE之后。

## WHERE子句操作符

操作符 | 说明 | 操作符 | 说明
- | - | - | -
= | 等于 | > | 大于
<> | 不等于 | >= | 大于等于
!= | 不等于 | !> | 不大于
< | 小于 | BETWEEN | 在指定的两值之间
<= | 小于等于 | IS NULL | 为NULL值
!< | 不小于 | |

* 并非所有DBMS都支持这些操作符。

## 不匹配检查
```
SELECT vend_id,prod_id,prod_names,prod_price
From Products
WHERE vend_id <>'DLL01'
ORDER BY prod_price,prod_names;
```

* **提示：**何时使用引号如果仔细观察上述WHERE子句中的条件，会看到有的值括在单引号内，而有的值未括起来。
单引号用来限定字符串。如果将值与字符串类型的列进行比较，就需要限定引号。用来与数值列进行比较的值不用引号。

## 范围值检查
```
SELECT prod_names,prod_price
From Products
WHERE prod_price BETWEEN 5 AND 10;
```
在使用BETWEEN时，必须指定两个值——所需范围的低端值和高端值。这两个值必须用AND关键字分隔。
BETWEEN匹配范围中所有的值，包括指定的开始值和结束值。

## 空值检查
```
SELECT cust_name
From Customers
WHERE cust_name IS NULL;
```

**注意：NULL和非匹配**
通过过滤选择不包含指定值的所有行时，你可能希望返回含NULL值的行。
但是这做不到。因为未知（unknown）有特殊的含义，数据库不知道它们是否匹配，所以在进行匹配过滤或非匹配过滤时，不会返回这些结果。
过滤数据时，一定要验证被过滤列中含NULL的行确实出现在返回的数据中。

**注意：**在同时使用ORDER BY和WHERE子句时，应该让ORDER BY位于WHERE之后。

# 5.组合WHERE子句
SQL允许给出多个WHERE子句。这些子句有两种使用方式，即以AND子句或OR子句的方式使用。

## AND操作符
要通过不止一个列进行过滤，可以使用AND操作符给WHERE子句附加条件。
```
SELECT vend_id,prod_names,prod_price
From Products
WHERE vend_id = 'DLL01' AND prod_price <= 4;
```










