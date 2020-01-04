from flask import Flask, request
import sqlite3

DATABASE = './app_data.db'

app=Flask(__name__)

def get_connection():
	global DATABASE
	conn=sqlite3.connect(DATABASE)
	return conn

@app.route("/set/",methods=["GET","POST"])
def set():
	key=request.args.get("key")
	value=request.args.get("value")

	conn=get_connection()
	
	with conn:
		conn.execute("insert or replace into data values('{}','{}');".format(key,value))
		conn.commit()
	
	print("----------------------------------------")
	print("set",{"key":key,"value":value})
	print("----------------------------------------")
	
	conn.close()
	
	return str("{}:{} stored sucessfully".format(key,value))

@app.route("/get/", methods=["GET"])
def get():
	key=request.args.get("key")
	
	conn=get_connection()
	
	with conn:
		data=conn.execute("select data_key, data_value from data where data_key = '{}';".format(key))
	
	print("----------------------------------------")
	ans_key,ans_value = None, None
	for k1,v1 in data:
		ans_key=k1
		ans_value=v1
	print("get",{"key":key,"value":ans_value})
	print("----------------------------------------")
	
	conn.close()
	# check for None
	return str("{}".format(ans_value))

if(__name__=="__main__"):
	app.run(host="0.0.0.0", port= "5000" ,debug=False,threaded=True)