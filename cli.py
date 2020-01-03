import sys

command = sys.argv[1]
key = sys.argv[2]

if(command == "get"):
	print("get {}".format(key))

elif(command == "set"):
	value = sys.argv[3]
	print("set {} {}".format(key,value))	
