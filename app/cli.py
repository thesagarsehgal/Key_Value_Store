import sys

# inorder to make requests to the database 
import requests

# second argument would be to make a SET or GET request
if(len(sys.argv)>=2):
	# get the command from the first index
	command = sys.argv[1]
else:
	print("action to perform not provided")

# third argument would contain the key to query
if(len(sys.argv)>=3):
	# get the key from the second index
	key = sys.argv[2]
else:
	print("key not provided")

# get the URL of the API
API_URL="http://0.0.0.0:5000/"

# if the command 3 arguments i.e  the command and key are available 
if(len(sys.argv)>=3):

	if(command == "get"):
		
		# send request to the API and with the parameters
		response = requests.get(url = "{}get/".format(API_URL), params = {'key': key}) 
		print(response.text)
		
	elif(command == "set"):
		
		# check if the value correspondig to the query is priovided
		if(len(sys.argv) >= 4):	
			value = sys.argv[3]

			# send request to the API and with the parameters
			response = requests.get(url = "{}set/".format(API_URL), params = {'key': key, 'value': value}) 
			print(response.text)
		
		else:
			print("value not provided")
	
	else:
		print("wrong command provided")

else:
	print("insufficient arguments provided")