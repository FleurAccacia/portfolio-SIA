import streamlit as st
# from data import CONTACT
import csv
import os
from datetime import datetime

st.title("How to Contact Me ?")

with st.form("contact"):
 name = st.text_input("Your name")
 email = st.text_input("Your email")
 message = st.text_area("Your message")
 sent = st.form_submit_button("Send") # True only on the run that follows the click
 
 
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
            
            
        