import streamlit as st
import csv
import os
from datetime import datetime
import pandas as pd
from geopy.geocoders import Nominatim
from data import PROFILE


st.title("How to Contact Me ?")

left, right = st.columns([1, 2])
with left:
    st.write("""Have a project in health or AI, an opportunity, or a question?
             
Send me a message, I usually reply within 48 hours.""")

    @st.cache_data
    def get_coordinates(city):
        place = Nominatim(user_agent="portfolio-gracia").geocode(city)
        return (place.latitude, place.longitude) if place else None

    coords = get_coordinates(PROFILE["city"])

    if coords:
        df_map = pd.DataFrame({"lat": [coords[0]], "lon": [coords[1]]})
        st.map(df_map, latitude="lat", longitude="lon", zoom=10, size=800, color="#1f4fd8")

with right:
    with st.form("contact"):
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        message = st.text_area("Your message")
        sent = st.form_submit_button("Send") 
 
 
def save(name, email, message)  :
    file_exists = os.path.exists("messages.csv")
    with open("messages.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "name", "email", "message"])
        writer.writerow([datetime.now(), name, email, message])
             

#verifier les informations du formulaire
def check(name, email,message):
    problems = []
    if not name:
        problems.append("Name is empty")
    if "@" not in email or "." not in email.split("@")[-1]:
        problems.append("Email is invalid")
    if len(message) < 10:
        problems.append("Message is too short")
    return problems

# Si le formulaire est envoyé, vérifier les informations et afficher les erreurs ou le succès.
if sent:
        problems = check(name, email, message)
        if problems:
            for problem in problems:
                st.error(problem)
        else:
            st.success("Message sent successfully!")
            save(name, email, message)
            
            
        