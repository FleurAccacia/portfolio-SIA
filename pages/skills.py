import streamlit as st
from data import SKILLS
from data import TIMELINE
import pandas as pd
import numpy as np

st.title("My different Skills")

tab1, tab2 = st.tabs(["Skills", "Education"])
with tab1:
    for name , level in SKILLS.items():
        st.write(f"{name}")
        st.progress(level / 100) # Affiche une barre de progression pour chaque compétence
        
    df = pd.DataFrame({"name": list(SKILLS.keys()), "level": list(SKILLS.values())}) 
    st.divider() 
    st.bar_chart(df, x="name", y="level", color="green")  # Affiche un diagramme en barres de toutes les compétences
    
with tab2:
    # st.write("")
    columns = st.columns(2) 
    for i , (year, title) in enumerate(TIMELINE):
        with columns[i % 2]: 
            with st.container(border= True):
                st.subheader(title)        
                st.caption(f"Year: {year}")
            