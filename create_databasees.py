import mysql.connector
import os
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')

conn = mysql.connector.connect(host="localhost", user=username, password=userpass)
cur = conn.cursor()
cur.execute(""" CREATE DATABASE IF NOT EXISTS green""")
cur.close()
conn.commit()
conn.close()

conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
cur = conn.cursor()
print('Databse is created')
cur.execute("""CREATE TABLE IF NOT EXISTS `memberinfo` (
  `id` bigint DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `middle_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `blood_group` char(4) DEFAULT NULL,
  `nomine` varchar(255) DEFAULT NULL,
  `data_of_brith` date DEFAULT NULL,
  `data_of_joing` date DEFAULT NULL,
  `addherNo` bigint NOT NULL,
  `accountNo` varchar(255) DEFAULT NULL,
  `mobile_no1` bigint DEFAULT NULL,
  `mobile_no2` bigint DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `opning_balance` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`addherNo`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `key106_idx` (`mobile_no1`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci""")
cur.close()
conn.commit()
conn.close()

conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS `lone` (
  `lone_no` bigint NOT NULL,
  `appliername` varchar(255) DEFAULT NULL,
  `addherNo` bigint DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `insrast_rate` decimal(10,0) DEFAULT NULL,
  `check_number` varchar(255) DEFAULT NULL,
  `lone_date` date DEFAULT NULL,
  `Jamindar1` varchar(255) DEFAULT NULL,
  `Jamindar2` varchar(255) DEFAULT NULL,
  `remark` text,
  PRIMARY KEY (`lone_no`),
  KEY `key126_idx` (`addherNo`),
  CONSTRAINT `key126` FOREIGN KEY (`addherNo`) REFERENCES `memberinfo` (`addherNo`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci""")
cur.close()
conn.commit()
conn.close()

conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS `lone_info` (
  `Lone_no` bigint NOT NULL,
  `Name` varchar(255) NOT NULL,
  `AddherNo` bigint NOT NULL,
  `Lone_take` int NOT NULL,
  `Intrest` decimal(10,0) NOT NULL,
  `January` decimal(10,0) DEFAULT NULL,
  `interest_Jan` decimal(10,0) DEFAULT NULL,
  `February` decimal(10,0) DEFAULT NULL,
  `interest_feb` decimal(10,0) DEFAULT NULL,
  `March` decimal(10,0) DEFAULT NULL,
  `interest_mar` decimal(10,0) DEFAULT NULL,
  `April` decimal(10,0) DEFAULT NULL,
  `interest_apr` decimal(10,0) DEFAULT NULL,
  `May` decimal(10,0) DEFAULT NULL,
  `interest_may` decimal(10,0) DEFAULT NULL,
  `June` decimal(10,0) DEFAULT NULL,
  `interest_jun` decimal(10,0) DEFAULT NULL,
  `July` decimal(10,0) DEFAULT NULL,
  `interest_jul` decimal(10,0) DEFAULT NULL,
  `August` decimal(10,0) DEFAULT NULL,
  `interest_aug` decimal(10,0) DEFAULT NULL,
  `September` decimal(10,0) DEFAULT NULL,
  `interest_sep` decimal(10,0) DEFAULT NULL,
  `October` decimal(10,0) DEFAULT NULL,
  `interest_oct` decimal(10,0) DEFAULT NULL,
  `November` decimal(10,0) DEFAULT NULL,
  `interest_nov` decimal(10,0) DEFAULT NULL,
  `December` decimal(10,0) DEFAULT NULL,
  `interest_dec` decimal(10,0) DEFAULT NULL,
  `total_ammount_to_pay` int NOT NULL,
  `Total_interest_pay` int NOT NULL,
  `Total_interest_amount` int NOT NULL,
  PRIMARY KEY (`Lone_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci""")
cur.close()
conn.commit()
conn.close()
print("all stament executed")
