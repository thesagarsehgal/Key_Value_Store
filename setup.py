import sqlite3
conn = sqlite3.connect('./app_data.db')
conn.execute("create table data ( data_key VARCHAR(50) PRIMARY KEY NOT NULL, data_value INT NOT NULL);")
conn.close()