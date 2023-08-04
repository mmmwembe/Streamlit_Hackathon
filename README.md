# Streamlit Connection Hackathon 🔗

![Alt text](mongostream.png)

This connection is build on the top of the python framework **`Streamlit`** and **`Mongodb`**. It allows user to connect your mongodb cluster or local connection in just **7** lines of code. 


---

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

## Note: 
Add `local_connection_string` if `connection_string` is not added. That means you are doing your database connection in your local system. If you do your work in local system, remove the `connection_string` , `mongo_password` & `mongo_username`

