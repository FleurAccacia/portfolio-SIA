import streamlit as st
from data import PROJECTS

st.title("My Projects")

def all_tags(PROJECTS):
    tags = set()
    for project in PROJECTS:
        for tag in project["tags"]:
            tags.add(tag)
    return (sorted(tags))    

def filter_projects(PROJECTS, chosen):
    if not chosen:
        return PROJECTS
    filtred = []
    for project in PROJECTS:
        if any(tag in project["tags"] for tag in chosen):
            filtred.append(project)
    return filtred        

col_tags , col_sort = st.columns(2)
with col_tags:
    chosen_tags = st.multiselect("filter by tags", all_tags(PROJECTS))
    
filtered_projects = filter_projects(PROJECTS, chosen_tags) # filtre les projets en fonction des tags choisis

with col_sort:
    sort_order = st.selectbox("Sort by year", ("Most recent", "Oldest"))
if sort_order == "Most recent":
    filtered_projects = sorted(filtered_projects, key= lambda p: p["year"], reverse=True)
else:
    filtered_projects = sorted(filtered_projects, key= lambda p: p["year"])  


columns = st.columns(2) # permet d'afficher les projets en deux colonnes
for i , project in enumerate(filtered_projects):
    with columns[i % 2]: 
        with st.container(border= True):
            st.subheader(project["title"])
            st.write(project["description"])
            st.write(f"Tags: {', '.join(project['tags'])}")
            st.caption(f"Year: {project['year']}")
            st.link_button("See Project", project["link"]) # ajoute un bouton pour voir le projet
st.write(f"{len(filtered_projects)} project(s) found")             

