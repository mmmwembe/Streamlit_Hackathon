from connect import MongoDBConnection
import streamlit as st
import pandas as pd
import json
# connection object
conn = st.experimental_connection("mongodb", type=MongoDBConnection)
con, cursor = conn.cursor(db="mydb", col="games", query={})
docs = conn.showData(cursor=cursor)

document = st.text_input(label="Enter your query here")
if document:
    document_dict = json.loads(str(document))
if st.button('Enter'):
    c = conn.create(con=con, db="mydb", col="games", query=document_dict)
    if c:
        st.write("Document inserted")
    else:
        st.write("Document not inserted")
if st.button('Show data'):
    df = pd.DataFrame(docs)
    df['name'] = df['name:'].fillna('') + df['name'].fillna('')
    df.drop(columns=['name:'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    st.write(df)
    print(pd.DataFrame(df))


