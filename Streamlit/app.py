import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sn
import os
from streamlit.errors import Error

@st.cache(persist=True)

def load_data(nrows):

  data = pd.read_csv("pokemon.csv", nrows = nrows)
  return data

data = load_data(10)

st.subheader("Raw data de 10")
st.write(data)



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

st.header("TEST BUTTON")

st.button("simple button")

st.text("checkbox")
if st.checkbox("show/hide"):
  #Do Action
  st.text("some action")


status = st.radio("ton statut", ('active', 'Inactive'))
if status == 'active':
  st.success("tu es active")
else:
  st.warning("non active !")
st.text("boite de selection")


occupation = st.selectbox("ton poste", ['Développeur', 'analyste', 'Doctor'])
st.write("So, you are a ", occupation)

st.write("selection multiple")
location = st.multiselect("ou est tu ?", ("Paris", "Londre", "New York"))
st.write("You Selected", len(location), "location")