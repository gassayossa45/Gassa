import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
import warnings
import sys
import streamlit as st  # type: ignore

st.set_page_config(page_title="Gassa", layout="wide")
st.divider()
st.header("Progekt Streamlit")
st.divider()
st.sidebar.write(":red[Navigation]")

x,y,z = st.columns(3)
x.write("Name")
y.write("Vorname")
z.write("Email")
start = y.container()
start.write("Das ist ein Container")
st.write("Nach dem Container")
start.write("Das ist wieder in Contairner")
popover = start.popover("Das ist ein popower")
popover.write("Im Popover")
popover.write("Noch ein Popover")
testbutton = z.button("Test Button")
if testbutton == True:
    x.write("Du hast ein Button geklickt")
toller = x.toggle("Test Toggle")
if toller == True:
    x.write("Du hast ein Button geklickt")
slider = st.slider("Das ist ein Slider", value=(12,25))
Fruit = y.multiselect("Fruits",['Banane', 'Orange','Mangos'])
#Number = x,y,z = st.columns(3)
x.pills("Nombre",[1, 2,3])
selectbox = z.selectbox("Villes",['Los Angeles', 'Douala','Yaounde'])
x.write(selectbox)