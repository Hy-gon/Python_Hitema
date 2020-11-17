import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sn

 # DATA IMPORT
#@st.cache
#def load_data(URL):
 #   data=pd.read_csv(URL)
  #  return data

#path1=""
#selected=0

st.title("Streamlit Training")
st.header("Load CSV")

x = st.slider('x')
st.write(x, 'squared is', x * x)
