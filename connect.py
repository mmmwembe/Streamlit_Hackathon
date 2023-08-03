from streamlit.connections import ExperimentalBaseConnection
import pymongo 
import urllib 
from pymongo.server_api import ServerApi
from streamlit.runtime.caching import cache_data
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
    # @cache_data(ttl=3600)
    def cursor(_self, **kwargs) -> pymongo.MongoClient:
        db = kwargs['db']
        col = kwargs['col']
        query = kwargs['query']
        con = _self._connect()
        return con[db][col].find(query)
    
    def showData(self, **kwargs) -> pd.DataFrame:
        data = []
        for i in kwargs['cursor']:
            data.append(i)
        return pd.DataFrame(data)
    