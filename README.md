# Key Value Store

### How to run the Application

1. Clone the Github repo 
```
git clone https://github.com/sagar-sehgal/Key_Value_Store
```

2. Create a virtual enviornment
```
virtualenv venv --python=python3
```

3. Shift to the virtualenv 
```
source venv/bin/activate
```

4. Install the dependencies
```
pip install -r Key_Value_Store/requirements.txt
```

5. Shift to the `Key_Value_Store` directory
```
cd Key_Value_Store
```

6. Build the docker container
```
docker-compose build
```

7. Start the docker container
```
docker-compose up
```
This will start the applocation at `0.0.0.0:5000`.

### Run directly from DockerHub

0. Install docker in the system
1. Get the docker-image
```
docker pull sagarsehgal/sagar_key_value_store
```
2. Run the docker-container
```
docker run -p 5000:5000 -t sagarsehgal/sagar_key_value_store:latest
```
This will run the application a


### Test the Application

0. Shift to the `Key_Value_Store` directory
```
cd Key_Value_Store
```

1. To run the tests
```
python3 app/tests/test.py
```

### Working with the CLI

0. Shift to the `Key_Value_Store` directory
```
cd Key_Value_Store
```

1. Build the docker container
```
docker-compose build
```

2. Start the docker container
```
docker-compose up
```
This will start the applocation at `0.0.0.0:5000`.

Now we can run the application a command line application which will send request to the flask application.

The format of the CLI is =>
```
python3 cli.py [COMMAND] [KEY] [VALUE] 
```

The commands for the CLI are as follows:-

1. To reset the database 
```
python3 cli.py reset

[Output]: 
key not provided
Database Reset
```

2. Get the value of the key if the key is not present
```
python3 cli.py get k1

[Output]: 
None
```

3. Set the value of the key 
```
python3 cli.py set k1 v1

[Output]: 
k1:v1 stored sucessfully
```

6. Get the value of the key if the key is present
```
python3 cli.py get k1

[Output]: 
v1
```

7. Reset the value of the key, even thouh the value if already present. This would overrite the value for that key.
```
python3 cli.py set k1 v2

[Output]: 
k1:v2 stored sucessfully
```

8. Get the value for a given key, after replacing it. It returns the updated value of the key.
```
python3 cli.py get k1

[Output]: 
v2
```

### About the Application

**Tech Stack** 
- Python
- Docker
- Flask 
- Gunicorn

The Application has the following features:-

#### 1. RESET
- Resets the database. It drops the table that stores the key value pair and recreates it.

#### 2. GET
- **input=>** 		given a key
- **processing=>** 	retrievies the key value from the database
- **output=>** 		return the value corresponding to the key

- Gets the value corresponding to the key.
- For this a SQL query is fired on SQLITE, to get the value.
- For querying over the databse, the database is locked first.
- If the key is not present, returns `None`

#### 3. SET
- **input=>** 		key and value taken as input from the request
- **processing=>** 	stores the key and value pair in the database
- **output=>** 		returns a string validating that the key,value pair has been added

- Sets the value corresponding to the key.
- For this a SQL query is fired on SQLITE, to set the key,value pairs.
- For querying over the databse, the database is locked first.
- If the key is already present, overrites the previous value.

#### Others
- The app has been **Dockerized**, making it easy to deploy
- Also, the the Flask app now works with **Gunicorn** with 4 workers.
- Also, the `cli.py` send the request to the module, with the parameters, along with the request, in order to save and retrive the key,value pairs.