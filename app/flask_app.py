from flask import Flask, request

# importing sqlite3 ... bcz woud be using SQLite to store the key value pairs
import sqlite3

# the database name
DATABASE = './app_data.db'

# initializing the application 
app=Flask(__name__)

# a function to get connection to the database
def get_connection():
	''' gets connected to the database and returns the coonection variable '''
	global DATABASE
	conn=sqlite3.connect(DATABASE)
	return conn

# function to set the key,value pairs .... uses GET and POST both methods
@app.route("/set/",methods=["GET","POST"])
def set():
	'''sets the keys and value pairs'''

	# gets the key from the request which was recieved
	key = request.args.get("key")
	# gets the key from the request which was recieved
	value = request.args.get("value")

	# gets the connection to the database
	conn = get_connection()
	
	# locking the databse
	with conn:
		# execute the statment to update/insert a key value pair.
		# If the key would exist already, then it would be updated to the new value,
		# else a new key would be formed with the corresponding value  
		conn.execute("insert or replace into data values('{}', '{}');".format(key, value))
		
		# commiting the changes the in the above statement 
		conn.commit()
	
	print("----------------------------------------")
	print("set",{"key":key,"value":value})
	print("----------------------------------------")
	
	# closing the connection with the databse
	conn.close()
	
	# return the  corresponding statement
	return str("{}:{} stored sucessfully".format(key, value))

# function to get the key,value pairs .... uses only GET method .... bcz the database would only be read
@app.route("/get/", methods=["GET"])
def get():
	'''gets the value for a giccen key '''

	# gets the key from the request which as recieved
	key = request.args.get("key")
	
	# gets the connection variable
	conn = get_connection()
	
	# locking the database
	with conn:
		# sql quesry to query over the database for the given key
		data = conn.execute("select data_key, data_value from data where data_key = '{}';".format(key))
	
	print("----------------------------------------")	
	# sets the key and the value to be None  
	ans_key, ans_value = None, None

	# iterates over ros to get the key and value
	for k1,v1 in data:
		ans_key=k1
		ans_value=v1
	
	# if there was no such key, then the value corresponding to it would be None

	print("get",{"key":key,"value":ans_value})
	print("----------------------------------------")
	
	# close the connection to the database
	conn.close()
	
	# return the corresponding statement
	return str("{}".format(ans_value))

if(__name__=="__main__"):
	# run the app at 0.0.0.0 on porn no. 5000
	app.run(host="0.0.0.0", port= "5000" ,debug=False,threaded=True)