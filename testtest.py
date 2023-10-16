import streamlit as st
import pyodbc
def main_page():
    st.title('Rental Equipment Correlation Analysis')    
    import pandas as pd
    # Initialize connection.
    def init_connection():
        return pyodbc.connect(
            "DRIVER={SQL Server};SERVER="
            + st.secrets["server"]
            + ";DATABASE="
            + st.secrets["database"]
            + ";UID="
            + st.secrets["username"]
            + ";PWD="
            + st.secrets["password"]
        )
    
    conn = init_connection()
    
    # Perform query.
    def run_query(query):
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()
    
    rows = run_query("SELECT Job from JCM_MASTER__JOB;")
    
    # Print results.
    for row in rows:
        st.write(f"{row[0]} has a :{row[1]}:")
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
