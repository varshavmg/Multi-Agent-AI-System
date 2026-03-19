import streamlit as st
import requests

st.title("Multi Agent AI Research System")

topic = st.text_input("Enter topic")

if st.button("Generate Research"):

    response = requests.post(
        "http://localhost:8000/research",
        json={"topic": topic}
    )

    data = response.json()

    st.write("Plan:")
    st.write(data["plan"])

    st.write("Report:")
    st.write(data["report"])