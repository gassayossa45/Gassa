import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#import seaborn as sns
import numpy as np
import warnings
import sys
import streamlit as st  # type: ignore

#Data import
data = pd.read_csv('DAXDataStreamlit.csv')
st.set_page_config(page_title="DAX-Analyse", layout="wide")
st.header("Progekt Aktien-Analyse")
#Sidebar
st.sidebar.header(":red[Sidebar]")
st.sidebar.write("Hier kannst du die zu analysierenden Aktien auswählen:")

#Aktien Auswahl
selected_stock = st.sidebar.pills("Auswahl",data.iloc[:,1].drop_duplicates(),selection_mode="multi")
stock_filtered_data = data[data.iloc[:,1].isin(selected_stock)]

#
with st.popover("Zeit-Einstellungen"):
    st.slider("Wähle den Zeitraum aus", 1, 5)
    
#x,y = st.columns([1,5])
#zeit = x.multiselect("",("Zeit_einstellung"),placeholder="Zeit_einstellung")
#if "Zeit_einstellung" in zeit:
    #zeitraum = x.slider(
        #"wählt ein Zeitraum aus:",
        #min_value=0,
        #max_value=5,
       # value=2,          # Standardwert
        #step=1
    #)
with st.popover("Metrik-Auswahl"):
    metric = st.selectbox("Wähle die darzustellende Metrik",["Open","High","Low","Close","Volume"],index=3)    

#multuple_auswahl = x.multiselect("",[1,2,3],placeholder="Metrik-Auswhal")
#st.write("### Projekt Dax Analyse")
#st.write("Mit diesem App kannst du die letzte sechs Monate des Dax \U0001F4C8 analysieren 📊")
#a,b = st.columns([3,1]) 
#toller = a.toggle("DataFrame anzeigen: ")
#b.write("#### Analyse-Tools")
#b.selectbox("Welcher Wert?",[1, 2,3])
#st.sidebar.write(":red[Sidebar]")
#st.sidebar.write("Hier kannst du die zu analysiereden Aktien auswhälen: ")
#st.sidebar.write("Aktien auswhälen: ")
#st.sidebar.pills("Auswahl",[1, 2,3])
col1_graph, col2_tools = st.columns([3, 1])

with col1_graph:
    if selected_stock:
        fig,ax = plt.subplots(figsize=(10,6))
        for stock in selected_stock:
            stock_data = stock_filtered_data[stock_filtered_data.iloc[:,1] == stock]
            ax.plot(stock_data.iloc[:,2],stock_data.loc[:,metric], label = stock)
        #Graph configuration
        data["Date"] = pd.to_datetime(data["Date"])


        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%y-%m-%d"))
        plt.xticks(rotation=45)
        ax.set_title("Aktien Preise in Zeitverlauf")
        ax.set_xlabel("Datum")
        ax.set_ylabel("Preis in (€)")
        ax.legend()
        ax.grid(True)
        plt.tight_layout()
        st.pyplot(fig)

    else :
        st.write("Wähle Aktien aus der Sidebar aus: ")
    if st.toggle("Dataframe anzeigen:"):
        st.dataframe(stock_filtered_data)


with col2_tools:
    st.header("Analyse-Tools")
    st.selectbox("Welcher Wert?", [1, 2, 3])
    st.image("lebenslauf.jpg",width=200,channels="RGB", caption="Ich bin der Owner")
    st.video("https://www.youtube.com/watch?v=g5imnbSwZEU&pp=ugUEEgJmcg%3D%3D")