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

st.header("TEST TEXT")

st.subheader("A SubHeader")

st.sidebar.header("example SideBar")
st.sidebar.text("Text Sidebar 1")
st.sidebar.text("Text Sidebar 2")
st.sidebar.text("Text Sidebar 3")

st.text("Just a Text")

st.markdown("#### Markdown")

st.success("fully success")

st.info("info alert")

st.warning("WARNING")

st.error("this is a ERROR")

st.write("Write Here")

st.write("Python Range with WRITE", range(10))

st.text("Display JSON")
dico={
  'name':"saphiros",
  'age':24
}
st.json(dico)
