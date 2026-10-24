import streamlit as st
print("run")
st.title("Hello!")
name = st.text_input("What is your name?")
if name:
 st.write(f"Nice to meet you, {name}.")
 
age = st.slider("Your age", 15, 70, 20) 

if age<30 :
    st.write(f"you have 30 in {30-age} years")
else:
    st.write(f"you have been 30 for {age-30} years")    
 
# Q1:  Combien de fois est-il affiché dans le terminal ? Expliquez
# R : Le "Run" s'affiche 2 fois . Il s'incrémente à chaque fois que je change le nom et que j'execute
# Explication : Streamlit réexcute le fichier a chaque fois . 
 