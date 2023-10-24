import streamlit as st  
import pyodbc
def main_page():
    st.title('Rental Equipment Correlation Analysis')    
    import numpy as np
    import pandas as pd
    from SQLAlchemy import create_engine
    from sklearn.neighbors import NearestNeighbors
    import pyodbc
    import pymysql
    
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
