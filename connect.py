from streamlit.connections import ExperimentalBaseConnection
import pymongo 
import urllib 
from pymongo.server_api import ServerApi

class MongoDBConnection(ExperimentalBaseConnection[pymongo.MongoClient]):
    def _connect(self, **kwargs) -> pymongo.MongoClient:
        if 'connection_string' in kwargs:
            connection = kwargs.pop('connection_string')
        else:
            if(self._secrets.password and self._secrets.username):
                PASSWORD = urllib.parse.quote(self._secrets.mongo_password)
                USERNAME = urllib.parse.quote(self._secrets.mongo_username)
                connection = "mongodb+srv://" + USERNAME + ":" + PASSWORD + self._secrets.connection_string  
            else:    
                connection = self._secrets.local_connection_string  
        return pymongo.MongoClient(connection, server_api=ServerApi('1'))


#================== important part ==================







