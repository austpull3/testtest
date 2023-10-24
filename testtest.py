import streamlit as st  
import pyodbc
def main_page():
    st.title('Rental Equipment Correlation Analysis')    
    import numpy as np
    import pandas as pd
    import pyodbc

def page2():
    st.title("Exploratory Data Analysis")
    st.dataframe()
    
''' server = 'HOWE-ACCT-SERV\SAGE300CRE'
database = 'HoweInc'
username = 'sa'
password = 'L+S3jr3fP@*1'
'''
    
# Create a connection string
#connection_string = f"DRIVER={SQL Server};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    
# Establish a connection
conn = pyodbc.connect(driver = '{ODBC Driver 15 for SQL Server}', server = 'HOWE-ACCT-SERV\SAGE300CRE', database = 'HoweInc', uid = 'sa', password = 'L+S3jr3fP@*1')
    
cursor = conn.cursor()
    
query = "USE [HoweInc]"
result = cursor.execute(query)
#dict for pages
page_names_to_funcs = {
    "Welcome Page": main_page,
    "Data Exploration and Visualization": page2
    }
    #select pages
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
