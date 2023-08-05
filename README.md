# Streamlit Connection Hackathon 🔗

![Alt text](mongostream.png)

This connection is build on the top of the python framework **`Streamlit`** and **`Mongodb`**. It allows user to connect your mongodb cluster or local connection in just **7** lines of code. 


---

## Source Code Explanation
```
from streamlit.connections import ExperimentalBaseConnection
import pymongo 
import urllib 
from pymongo.server_api import ServerApi
import pandas as pd

class MongoDBConnection(ExperimentalBaseConnection[pymongo.MongoClient]):
    def _connect(self, **kwargs) -> pymongo.MongoClient:
        if 'connection_string' in kwargs:
            connection = kwargs.pop('connection_string')
        else:
            if(self._secrets.mongo_password and self._secrets.mongo_username):
                PASSWORD = urllib.parse.quote(self._secrets.mongo_password)
                USERNAME = urllib.parse.quote(self._secrets.mongo_username)
                connection = "mongodb+srv://" + USERNAME + ":" + PASSWORD + self._secrets.connection_string  
            else:    
                connection = self._secrets.local_connection_string  
        return pymongo.MongoClient(connection, server_api=ServerApi('1'))
    def cursor(_self, **kwargs) -> pymongo.MongoClient:
        db = kwargs['db']
        col = kwargs['col']
        query = kwargs['query']
        con = _self._connect()
        cursor = con[db][col].find(query)
        return con, cursor
    

    def create(_self, **kwargs) -> pymongo.MongoClient:
        db = kwargs['db']
        col = kwargs['col']
        query = kwargs['query']
        con = kwargs['con']
        return con[db][col].insert_one(query)
        
    def showData(self, **kwargs) -> pd.DataFrame:
        data = []
        for i in kwargs['cursor']:
            i.pop('_id', None)
            data.append(i)
        return data
```    
### Connection Method
- This method is used to established the connection object with MongoDB
  The users may use their local system to run MongoDB on `port 27017`(nested else statement of else method will be called for that) or `MongoDB Atlas`(nested if statement of else statement will be called for that)
```
def _connect(self, **kwargs) -> pymongo.MongoClient:
        if 'connection_string' in kwargs:
            connection = kwargs.pop('connection_string')
        else:
            if(self._secrets.mongo_password and self._secrets.mongo_username):
                PASSWORD = urllib.parse.quote(self._secrets.mongo_password)
                USERNAME = urllib.parse.quote(self._secrets.mongo_username)
                connection = "mongodb+srv://" + USERNAME + ":" + PASSWORD + self._secrets.connection_string  
            else:    
                connection = self._secrets.local_connection_string  
        return pymongo.MongoClient(connection, server_api=ServerApi('1'))
```
### Cursor Method
```
 def cursor(_self, **kwargs) -> pymongo.MongoClient:
        db = kwargs['db']
        col = kwargs['col']
        query = kwargs['query']
        con = _self._connect()
        cursor = con[db][col].find(query)
        return con, cursor
```
### Documents Creation Method
```
def create(_self, **kwargs) -> pymongo.MongoClient:
        db = kwargs['db']
        col = kwargs['col']
        query = kwargs['query']
        con = kwargs['con']
        return con[db][col].insert_one(query)
```
### Show Documents Method
```
def showData(self, **kwargs) -> pd.DataFrame:
        data = []
        for i in kwargs['cursor']:
            i.pop('_id', None)
            data.append(i)
        return data
```


## How to use this feature?
To use this feature you need to install few packages in your system by the following commands


1. `pip install streamlit`
2. `pip install pymongo`
3. `pip install pandas`

or you can do this in your terminal after cloning this repo

`pip install -r requirements.txt`

After successful installation clone this repo by using the following command👇🏻

`git clone <https://github.com/SoumyadeepOSD/Streamlit_Hackathon.git>`
 

 and add `.streamlit/secrets.toml` file in the root directory of the project folder

 and add the following code 👇🏻

 ```
[connections.mongodb]
connection_string = "@cluster0.xxxxxxxx"  // This is the connection string without <username> and <password>
mongo_password = "mongodb_password"
mongo_username = "mongodb_username"
local_connection_string = "mongodb://127.0.0.1:27017"
 ```

secrets.toml file should be looked like this
![image](https://github.com/SoumyadeepOSD/Streamlit_Hackathon/assets/115442240/abbbab44-5dc4-4116-a3c0-4e4bf1a0e6f0)


## Note: 
Add `local_connection_string` if `connection_string` is not added. That means you are doing your database connection in your local system. If you do your work in local system, remove the `connection_string` , `mongo_password` & `mongo_username`

If you are working with localhost, then your `secrets.toml` file should look like this
![image](https://github.com/SoumyadeepOSD/Streamlit_Hackathon/assets/115442240/8ed53795-5cf0-4e1d-9f0f-682d9d6780dd)


# Connection components

After cloning this repository, make a new python file in a separate folder and paste this following code

```from connect import MongoDBConnection
import sys
sys.path.insert(1, r"PATH_OF_<connect.py>")

# Make sure to add this two lines👆🏻, otherwise you will get 'No Module found error'

import streamlit as st
conn = st.experimental_connection("mongodb", type=MongoDBConnection)
con, cursor = conn.cursor(db="YOUR_DATABSE_NAME", col="COLLECTION_NAME", query={PUT YOUR MONGODB QUERY HERE FOR FINDING DOCUMENTS})
docs = conn.showData(cursor=cursor)
st.write(docs)
```
You will see this kind of output interface according to your database collection
![image](https://github.com/SoumyadeepOSD/Streamlit_Hackathon/assets/115442240/65abcb99-4d96-47aa-850e-3cf3ca4e2788)


If you want to insert query to the database, make sure to use this function
```
obj_creation = conn.create(db="YOUR_DATABSE_NAME", col="COLLECTION_NAME", query={PUT YOUR MONGODB QUERY HERE})
```
If you want to show the data, make sure to use this function
```
document_results = conn.showData(cursor=cursor)
```


**Here you go! You have successfully built the connection application between `MongoDB` and `Streamlit` 🎈**




