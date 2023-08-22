import pandas as pd 
import streamlit as st 
df=pd.read_excel('进销存.xlsx')
st.write(df)