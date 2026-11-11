import streamlit as st
from data import PROFILE, PROJECTS, SKILLS

st.title(f"Hi, I'm {PROFILE['name']}")
st.subheader(PROFILE["title"])

left, right = st.columns([1, 2])
with left:
 st.image("assets/photo.jpg", width=300)
 
 with open("assets/cv.pdf", "rb") as f:     
    if st.download_button("Download my CV", f, file_name="cv.pdf", type="primary"):
        st.badge("Download Successfully", icon=":material/check:", color="green")
 
with right:
 st.write(PROFILE["about"])
 #  st.write()
#  st.badge(f"{PROFILE['city']}", icon=":material/location_on:", color="orange")
#  st.badge(f"{PROFILE['email']}", icon=":material/email:", color="red")
#  st.badge(f"{PROFILE['linkedin']}", icon=":material/link:", color="blue")
BASE = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/icons"
BLUE = "filter: invert(25%) sepia(90%) saturate(3000%) hue-rotate(215deg) brightness(90%);"

st.markdown(
    f"""
    <div style="display:flex; gap:60px;justify-content:center; ">
        <a href="{PROFILE['github']}" target="_blank">
            <img src="{BASE}/github.svg" width="32" style="{BLUE}" >
        </a>
        <a href="{PROFILE['linkedin']}" target="_blank">
            <img src="{BASE}/linkedin.svg" width="32" style="{BLUE}" >
        </a>
        <a href="mailto:{PROFILE['email']}">
            <img src="{BASE}/envelope.svg" width="32" style="{BLUE}" >
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
 
#  st.write(f"{PROFILE['email']}")
#  st.write(f"{PROFILE['linkedin']}")


 
st.divider() 

col1, col2, col3 = st.columns(3)
col1.metric("Projects", len(PROJECTS))
col2.metric("Skills", len(SKILLS))
for skill in SKILLS:
    if SKILLS[skill] == max(SKILLS.values()):
        col3.metric("Best Skill", skill)

