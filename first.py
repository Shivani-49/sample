import streamlit as st
st.title("My First App")
data=pd.read_csv('big_mart')
st.dataframe(data)
