create database if not exists client_support;
use client_support;
CREATE TABLE if not exists client_queries (
    query_id VARCHAR(50) PRIMARY KEY,
    client_email VARCHAR(255) NOT NULL,
    client_mobile VARCHAR(20),
    query_heading VARCHAR(200),
    query_description TEXT,
    status ENUM('Open','Closed'),
    date_raised DATETIME,
    date_closed DATETIME
);
SELECT * FROM client_queries LIMIT 10;
select *from synthetic_client_queries limit 5;
show databases;	
create table  if not exists users(
   username TEXT,
   hashed_password TEXT,
   role TEXT
   );
   SELECT User, Host FROM mysql.user;
   DELETE FROM client_queries WHERE query_id = 'Q001';
   ALTER TABLE client_queries ADD image LONGBLOB;
