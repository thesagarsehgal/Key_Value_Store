from flask import Flask, request
import sqlite3

app=Flask(__name__)

@app.route("/set/")
def set():
	key=request.args.get("key")
	value=request.args.get("value")
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>set",key,value)
	return None

@app.route("/get/")
def get():
	key=request.args.get("key")
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>get",key)
	return None

if(__name__=="__main__"):
	app.run(debug=True)