import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Nos Villages Connectes - ANSUT",
    page_icon="📊",
    layout="wide"
)

# Titre principal
st.title("📊 Localisation des zones blanches")
st.markdown("**Tableau de bord interactif** - *by ANSUT*")

# Description (optionnelle)
st.markdown("---")
st.info("Ce tableau de bord présente l'état d'avancement des infrastructures en Côte d'Ivoire.")

# Intégration du rapport Power BI
powerbi_url = "https://app.fabric.microsoft.com/view?r=eyJrIjoiMTVjYjI3ODgtMDcxYi00YjNkLWIyNGYtMGQ0NDljZDQ0NTk2IiwidCI6Ijk1NDQ3ZDk4LThhYTEtNDdkOS04ODQyLTUyZGY2MzA0MTJiYSIsImMiOjh9"  # ← Remplacez par votre URL

st.components.v1.iframe(powerbi_url, width=1400, height=900, scrolling=True)

# Pied de page (optionnel)
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("📅 Dernière mise à jour", "Octobre 2025")
with col2:
    st.metric("🏢 Source", "ANSUT")
with col3:
    st.metric("🗺️ Pays", "Côte d'Ivoire")
st.markdown("© 2025 ANSUT - Tous droits réservés.")

