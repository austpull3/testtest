import streamlit as st  
import pyodbc
def main_page():
    st.title('Rental Equipment Correlation Analysis')    
    import pandas as pd
    # Initialize connection.
    server = 'HOWE-ACCT-SERV\SAGE300\Data\HOWE\'
    database = 'HoweInc'
    username = 'sa'
    password = 'L+S3jr3fP@*1'
        # Create a connection string
    connection_string = f"DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"
    
    # Establish a connection
    conn = pyodbc.connect(connection_string)
    
    cursor = conn.cursor()
    
    query = "USE [HoweInc]"
    result = cursor.execute(query)
def page2():
    st.title("Exploratory Data Analysis")
#dict for pages
page_names_to_funcs = {
    "Welcome Page": main_page,
    "Data Exploration and Visualization": page2
    }
    #select pages
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
