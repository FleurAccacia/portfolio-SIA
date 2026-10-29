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
#  st.write()
 st.badge(f"{PROFILE['city']}", icon=":material/location_on:", color="orange")
 st.badge(f"{PROFILE['email']}", icon=":material/email:", color="red")
 st.badge(f"{PROFILE['linkedin']}", icon=":material/link:", color="blue")
 
#  st.write(f"{PROFILE['email']}")
#  st.write(f"{PROFILE['linkedin']}")

with open("assets/cv.pdf", "rb") as f:     
    if st.download_button("Download my CV", f, file_name="cv.pdf", type="primary"):
        st.badge("Download Successfully", icon=":material/check:", color="green")
 
st.divider() 

col1, col2, col3 = st.columns(3)
col1.metric("Projects", len(PROJECTS))
col2.metric("Skills", len(SKILLS))
for skill in SKILLS:
    if SKILLS[skill] == max(SKILLS.values()):
        col3.metric("Best Skill", skill)

