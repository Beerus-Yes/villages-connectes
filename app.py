import streamlit as st

st.set_page_config(
    page_title="Zones Blanches - ANSUT",
    layout="wide"
)

# CSS pour optimiser l'affichage
st.markdown("""
    <style>
    .main {padding: 0rem 1rem;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Localisation des zones blanches - ANSUT")

powerbi_url = "https://app.fabric.microsoft.com/view?r=eyJrIjoiMTVjYjI3ODgtMDcxYi00YjNkLWIyNGYtMGQ0NDljZDQ0NTk2IiwidCI6Ijk1NDQ3ZDk4LThhYTEtNDdkOS04ODQyLTUyZGY2MzA0MTJiYSIsImMiOjh9"

st.components.v1.iframe(powerbi_url, height=1000, scrolling=True)