from flask import Flask, request
import sqlite3

DATABASE = './app_data.db'

app=Flask(__name__)

def get_connection():
	global DATABASE
	conn=sqlite3.connect(DATABASE)
	return conn

@app.route("/set/")
def set():
	key=request.args.get("key")
	value=request.args.get("value")
	conn=get_connection()
	conn.execute("insert or replace into data values('{}',{});".format(key,value))
	conn.commit()
	print("----------------------------------------")
	print({"key":key,"value":value})
	print("----------------------------------------")
	conn.close()
	return None

@app.route("/get/")
def get():
	key=request.args.get("key")
	conn=get_connection()
	data=conn.execute("select data_key, data_value from data where data_key = '{}';".format(key))
	print("----------------------------------------")
	for k,v in data:
		key=k
		value=v
		print({"key":key,"value":value})
	print("----------------------------------------")
	conn.close()
	return None

if(__name__=="__main__"):
	app.run(debug=True)