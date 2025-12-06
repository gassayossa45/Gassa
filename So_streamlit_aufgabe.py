import streamlit as st

st.set_page_config(
    page_title="DAX App",
    layout="wide"
)

st.sidebar.header("Sidebar")
st.sidebar.write("Hier kannst du die zu analysierenden Aktien auswählen:")
st.sidebar.pills("Auswahl", [1, 2, 3])


with st.popover("Zeit-Einstellungen"):
    st.slider("Wähle den Zeitraum aus", 1, 5)


with st.popover("Metrik-Auswahl"):
    st.selectbox("Wähle die darzustellende Metrik", [1, 2, 3])    


st.header("Projekt DAX-Analyse")
"Mit dieser App kannst du die letzten **sechs Monate** des DAX analysieren. :chart:"


col1_graph, col2_tools = st.columns([2, 1])

with col1_graph:
    st.toggle("Dataframe anzeigen:")


with col2_tools:
    st.header("Analyse-Tools")
    st.selectbox("Welcher Wert?", [1, 2, 3])