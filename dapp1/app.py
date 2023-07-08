import pandas as pd  
import numpy as np 
import streamlit as st
import plotly.express as px

# loading the data
@st.cache_data
def load_data():
    path = 'data/kc_house_data.csv'
    df = pd.read_csv(path)
    return df

# call the load_data function
with st.spinner('loading data...'):
    df= load_data()
    
st.title('House Price Data Analysis')
    
    
if st.checkbox('show dataset',True):
    st.subheader('Dataset')
    st.dataframe(df)