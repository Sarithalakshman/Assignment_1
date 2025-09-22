import streamlit as st
import pandas as pd
from uuid import uuid4
from db_operations import submit_query, login_user, view_queries, close_query

st.title("Client Query Management System")

# ---------------- LOGIN ----------------
username = st.text_input("Username")
password = st.text_input("Password", type="password")
role = None

if st.button("Login as Client"):
    role = login_user(username, password)

# ---------------- CLIENT QUERY FORM ----------------
if role != "Client":
    st.error("Only Clients can submit queries.")
elif role == "Client":
    st.subheader("Submit a New Query")

    with st.form(key="query_form"):
        email = st.text_input("Email")
        mobile = st.text_input("Mobile")
        heading = st.text_input("Query Heading")
        description = st.text_area("Query Description")
        uploaded_image = st.file_uploader("Upload Screenshot (optional)", type=["png","jpg","jpeg"])
        
        submit_button = st.form_submit_button("Submit Query")

        if submit_button:
            query_id = str(uuid4())[:8]
            image_data = uploaded_image.read() if uploaded_image else None
            submit_query(query_id, email, mobile, heading, description, image_data)
            st.success(f"✅ Query submitted successfully! Your Query ID: {query_id}")


st.subheader("Support Team Dashboard")


support_username = st.text_input("Support Username")
support_password = st.text_input("Support Password", type="password")
support_role = None


if st.button("Login as Support"):
    support_role = login_user(support_username, support_password)
if support_role != "Support":
    st.error("Only Support Team members can access this dashboard.")


if support_role == "Support":
    status_filter = st.selectbox("Filter by Status", ["All", "Open", "Closed"])

    if status_filter == "All":
        queries = view_queries()
    else:
        queries = view_queries(status_filter)

    df = pd.DataFrame(queries, columns=["ID","Email","Mobile","Heading","Description","Status","Date Raised","Date Closed","Image"])
    st.dataframe(df)

    query_to_close = st.selectbox("Select Open Query to Close", df[df['Status']=="Open"]['ID'])
    if st.button("Close Selected Query"):
        close_query(query_to_close)
        st.success(f"Query {query_to_close} closed!")

    for idx, row in df.iterrows():
        if row["Image"]:
            st.image(row["Image"], caption=f"Query {row['ID']} Screenshot")
    # Query Trends
    df['Date Raised'] = pd.to_datetime(df['Date Raised'])
    st.line_chart(df.groupby(df['Date Raised'].dt.date).size())


    # Resolution Times
    df['Resolution Time'] = (pd.to_datetime(df['Date Closed']) - pd.to_datetime(df['Date Raised'])).dt.total_seconds()/3600
    st.bar_chart(df.groupby('Heading')['Resolution Time'].mean())


    # Support Load / Backlogs
    st.bar_chart(df['Heading'].value_counts())