from connect import MongoDBConnection
import streamlit as st
from bson import ObjectId
import pandas as pd
# connection object
conn = st.experimental_connection("mongodb", type=MongoDBConnection)
# cursor object
query = {}
cursor = conn.cursor(db="test", col="chats", query={})
res = conn.showData(cursor=cursor)
st.write(res)
