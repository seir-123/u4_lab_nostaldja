-- settings.sql
CREATE DATABASE nos_db;
CREATE USER nos_dbuser WITH PASSWORD 'nos_db';
GRANT ALL PRIVILEGES ON DATABASE nos_db TO nos_dbuser;