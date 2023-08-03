from connect import MongoDBConnection
import streamlit as st
conn = st.experimental_connection("mongodb", type=MongoDBConnection)


# database_name = "mydb"

# database = client[database_name]

# # print(database)

# collection_name = "games"

# collection = database[collection_name]


# documents = collection.find()

# for i in documents:
print(conn._connect())



# import pymongo

# conn = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# print(type(conn))

# print(conn['mydb'])

# db = conn["mydb"]

# print(db)