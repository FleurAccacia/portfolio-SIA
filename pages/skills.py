import streamlit as st
from data import SKILLS
from data import TIMELINE
from data import CERTIFICATES
import pandas as pd
import numpy as np

st.title("My different Skills")

tab1, tab2 , tab3 = st.tabs(["Skills", "Education", "Certifications"])
with tab1:
    for name , level in SKILLS.items():
        st.write(f"{name}")
        st.progress(level / 100) # Affiche une barre de progression pour chaque compétence
        
    df = pd.DataFrame({"name": list(SKILLS.keys()), "level": list(SKILLS.values())}) 
    st.divider() 
    st.bar_chart(df, x="name", y="level", color="green")  # Affiche un diagramme en barres de toutes les compétences
    
# with tab2:
#     # st.write("")
#     columns = st.columns(2) 
#     for i , (year, title) in enumerate(TIMELINE):
#         with columns[i % 2]: 
#             with st.container(border= True):
#                 st.subheader(title)        
#                 st.caption(f"Year: {year}")
BASE = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/icons"
BLUE = "filter: invert(18%) sepia(60%) saturate(2500%) hue-rotate(215deg) brightness(90%);"


ICONS = ["mortarboard"]

CARD_CSS = """
<style>
.tl-card {
    background:#transparent; border:1px solid #e5e7eb; border-radius:20px;
    padding:28px 20px; text-align:center; height:100%;
    box-shadow:0 1px 3px rgba(0,0,0,0.05);
    border-style: solid; border-width: 1px; border-color: #6b2440;
}
.tl-icon {
    width:80px; height:80px; border-radius:50%;
    background:#f3f5f9; border:2px solid #dfe3ec;
    display:flex; align-items:center; justify-content:center;
    margin:0 auto 20px auto;
}
.tl-icon img { width:36px; height:36px; }
.tl-title { font-size:1.25rem; font-weight:700; color:#1f2937; margin-bottom:10px; }
.tl-period { color:#6b7280; font-size:1rem; }
</style>
"""

with tab2:
    st.markdown(CARD_CSS, unsafe_allow_html=True)
    columns = st.columns(2)
    for i, (period, title) in enumerate(TIMELINE):
        icon = ICONS[i % len(ICONS)]
        with columns[i % 2]:
            st.markdown(
                f"""
                <div class="tl-card">
                    <div class="tl-icon">
                        <img src="{BASE}/{icon}.svg" style="{BLUE}">
                    </div>
                    <div class="tl-title">{title}</div>
                    <div class="tl-period">{period}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

@st.dialog("Certificate", width="large")
def show_certificate(cert):
    st.image(cert["image"], use_container_width=True)
    st.caption(f"{cert['title']} · {cert['issuer']}")

with tab3:
    st.markdown(
        """
        <style>
        .st-key-certs div[data-testid="stImage"] img {
            height: 200px;
            object-fit: cover;
            object-position: top;
        }
        .cert-title { font-size:1.2rem; font-weight:700; margin:8px 0 4px 0; }
        .cert-issuer { color:#1f4fd8; margin-bottom:8px; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container(key="certs"):
        columns = st.columns(3)
        for i, cert in enumerate(CERTIFICATES):
            with columns[i % 3]:
                with st.container(border=True):
                    st.image(cert["image"], use_container_width=True)
                    st.markdown(f'<div class="cert-title">{cert["title"]}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="cert-issuer">{cert["issuer"]}</div>', unsafe_allow_html=True)
                    if st.button("Voir", key=f"cert_{i}", type="primary"):
                        show_certificate(cert)