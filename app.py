import streamlit as st
import google.generativeai as genai

# Gemini API Key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Kisan Saathi")

st.title("🌾 Kisan Saathi")
st.subheader("AI Farming Assistant")

question = st.text_input(
    "अपना सवाल पूछें / Ask your farming question"
)

if question:

    prompt = f"""
    You are an agriculture expert for Indian farmers.

    Answer in simple Hindi.

    Farmer Question:
    {question}
    """

    response = model.generate_content(prompt)

    st.write(response.text)
