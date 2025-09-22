# Assignment_1
Client Query Management system:
This project is a web-based application designed to manage client support queries. It is built using Python, Streamlit, and MySQL, with a clear separation of concerns across three main files.

app.py (Frontend): This is the main application file that creates the user interface using Streamlit. It provides a form for clients to submit queries and a dashboard for support staff to manage and track tickets.

db_operations.py (Backend): This file contains all the core functions for interacting with the MySQL database. It handles critical operations such as user authentication, query submission, and status updates, acting as the logic layer between the frontend and the database.

clientQMP.ipynb (Setup): A Jupyter Notebook used for the one-time initial setup of the project. It installs necessary dependencies, creates the initial client and support user accounts, and populates the database with a sample query for testing.
