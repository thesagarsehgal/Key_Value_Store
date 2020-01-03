import sys
import requests

if(len(sys.argv)>=2):
	command = sys.argv[1]
else:
	print("action not provided")

if(len(sys.argv)>=3):
	key = sys.argv[2]
else:
	print("key not provided")

API_URL="http://localhost:5000/"

if(len(sys.argv)>=3):
	if(command == "get"):
		# rep = requests.get("{}get/?key={}".format(API_URL,key))
		response = requests.get(url = "{}get/".format(API_URL), params = {'key': key}) 
		print(response.text)
		
	elif(command == "set"):
		if(len(sys.argv) >= 4):	
			value = sys.argv[3]
			# rep = requests.get("{}set/?key={}&value={}".format(API_URL,key,value))
			response = requests.get(url = "{}set/".format(API_URL), params = {'key': key, 'value': value}) 
			print(response.text)
		else:
			print("value not provided")
	
	else:
		print("wroong command provided")

else:
	print("insufficient arguments provided")