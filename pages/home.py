import streamlit as st
from data import PROFILE, PROJECTS, SKILLS
st.title(f"Hi, I'm {PROFILE['name']}")
st.subheader(PROFILE["title"])
left, right = st.columns([1, 2])
with left:
 st.image("assets/photo.jpg", width=220)
with right:
 st.write(PROFILE["about"])
 # TODO: city and e-mail, then a button to download assets/cv.pdf
 st.write(f"{PROFILE['city']}")
 st.write(f"{PROFILE['email']}")
 st.write(f"{PROFILE['linkedin']}")

with open("assets/cv.pdf", "rb") as f:     
    if st.download_button("Download my CV", f, file_name="cv.pdf"):
        st.write('Thanks for downloading!')
 
st.divider() 


