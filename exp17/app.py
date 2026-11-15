import streamlit as st
st.title("Streamlit Basics")
st.header("Section 1")
st.markdown("**Bold**, *italic*, and `code`.")
st.write("st.write handles many types automatically.")
import pandas as pd
df = pd.DataFrame({"name":["A","B","C"], "score":[90,75,88]})
st.dataframe(df)
st.table(df)
st.line_chart(df.set_index("name"))
st.bar_chart(df.set_index("name"))
name = st.text_input("Your name", "Student")
age = st.slider("Age", 18, 60, 25)
role = st.selectbox("Role", ["Student","Engineer","Teacher"])
st.write(f"Hello {name}, {role}, age {age}.")

if st.checkbox("Show data"):
    st.dataframe(df)
if st.button("Greet"):
    st.success(f"Welcome, {name}!")


nums = st.multiselect("Pick numbers", [1,2,3,4,5], [1,2])
d = st.date_input("Pick a date")
st.write("Selected:", nums, d)

@st.cache_data
def load():
    return pd.read_csv("bigfile.csv")
# data = load()