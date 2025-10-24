import streamlit as st

# 🧭 Paramètres de la page
st.set_page_config(page_title="🛰️ Zones Blanches ANSUT", layout="wide")

# 🧼 CSS — Suppression des espaces Streamlit
st.markdown("""
    <style>
    .main {padding: 0rem; margin: 0rem;}
    header {visibility: hidden;}
    .block-container {padding-top: 0rem; padding-bottom: 0rem;}
    .stApp > header {display: none;}
    .stApp > div:first-child {padding-top: 0rem;}
    </style>
    """, unsafe_allow_html=True)

# 🖼️ Iframe Power BI (plein écran)
iframe_code = """
<iframe 
    title="RealMapDDIR"
    width="100%"
    height="900"
    src="https://app.fabric.microsoft.com/view?r=eyJrIjoiMTVjYjI3ODgtMDcxYi00YjNkLWIyNGYtMGQ0NDljZDQ0NTk2IiwidCI6Ijk1NDQ3ZDk4LThhYTEtNDdkOS04ODQyLTUyZGY2MzA0MTJiYSIsImMiOjh9"
    frameborder="0"
    allowFullScreen="true"
    style="border:none; border-radius: 0px; overflow:hidden;">
</iframe>
"""

# 📊 Affichage dans Streamlit
st.components.v1.html(iframe_code, height=600)
