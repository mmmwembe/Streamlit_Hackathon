from connect import MongoDBConnection
import streamlit as st
# connection object
conn = st.experimental_connection("mongodb", type=MongoDBConnection)
# cursor object
query = { "price": { "$gt": 400 } }
cursor = conn.cursor(db="mydb", col="games", query=query)

res = conn.showData(cursor=cursor)
st.dataframe(res)
