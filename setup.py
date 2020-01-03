import sqlite3
conn = sqlite3.connect('./app_data.db')
conn.execute("drop table if exists data;")
conn.execute("create table data ( data_key VARCHAR(50) PRIMARY KEY NOT NULL, data_value VARCHAR(50) NOT NULL);")
conn.close()