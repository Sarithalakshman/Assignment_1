import mysql.connector
import hashlib
from datetime import datetime

# Database connection function
def get_connection():
    conn = mysql.connector.connect(
        host="localhost",        
        user="root",             
        password="srihari", 
        database="client_support"
    )
    return conn

# Function to register a new user
def register_user(username, password, role):
    conn = get_connection()
    cur = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    sql = "INSERT INTO users (username, hashed_password, role) VALUES (%s, %s, %s)"
    cur.execute(sql, (username, hashed_password, role))
    conn.commit()
    conn.close()
    print("✅ User registered successfully!")

# Function to log in a user
def login_user(username, password):
    conn = get_connection()
    cur = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    sql = "SELECT role FROM users WHERE username=%s AND hashed_password=%s"
    cur.execute(sql, (username, hashed_password))
    row = cur.fetchone()
    conn.close()

    if row:
        print(f"Login successfull Role: {row[0]}")
        return row[0]
    else:
        print(" Invalid username or password.")
        return None

# Function for a client to submit a new query
def submit_query(query_id, email, mobile, heading, description, image_data=None):
    conn = get_connection()
    cur = conn.cursor()
    date_raised = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Open"
    date_closed = None

    sql = """INSERT INTO client_queries 
            (query_id, client_email, client_mobile, query_heading, query_description, status, date_raised, date_closed, image)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    cur.execute(sql, (query_id, email, mobile, heading, description, status, date_raised, date_closed, image_data))
    conn.commit()
    conn.close()
    print("✅ Query submitted successfully!")

# Function for the support team to view queries
def view_queries(status=None):
    conn = get_connection()
    cur = conn.cursor()
    if status:
        cur.execute("SELECT * FROM client_queries WHERE status=%s", (status,))
    else:
        cur.execute("SELECT * FROM client_queries")
    rows = cur.fetchall()
    conn.close()
    return rows

# Function for the support team to close a query
def close_query(query_id):
    conn = get_connection()
    cur = conn.cursor()
    date_closed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = "UPDATE client_queries SET status=%s, date_closed=%s WHERE query_id=%s AND status='Open'"
    cur.execute(sql, ("Closed", date_closed, query_id))
    if cur.rowcount == 0:
        print("⚠️ Query not found or already closed.")
    else:
        conn.commit()
        print("✅ Query closed successfully.")
    conn.close()