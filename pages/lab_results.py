import streamlit as st
import pandas as pd

st.title("Lab results")

@st.cache_data
def load_results(path):
    return pd.read_csv(path)

df = load_results("assets/tp2_results.csv")

st.dataframe(df)
st.line_chart(
    df,
    x="n",
    y=["list", "numpy", "bst"],
    x_label="Number of values n",
    y_label="Average search time (s)",
)