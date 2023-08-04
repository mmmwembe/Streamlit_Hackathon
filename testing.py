from connect import MongoDBConnection
import streamlit as st
# connection object
conn = st.experimental_connection("mongodb", type=MongoDBConnection)
# cursor object
query = {}
cursor = conn.cursor(db="test", col="chats", query={})
res = conn.showData(cursor=cursor)
print(res)
