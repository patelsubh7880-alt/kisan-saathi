import streamlit as st
import google.generativeai as genai

# -------------------
# Page
# -------------------
st.set_page_config(
    page_title="Kisan Saathi",
    page_icon="🌾"
)

st.title("🌾 किसान साथी")
st.subheader("कृषि सलाह सहायक")

# -------------------
# API Key
# -------------------
API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=API_KEY)

# Stable model
model = genai.GenerativeModel("gemini-1.5-flash")

# -------------------
# Input
# -------------------
query = st.text_input(
    "अपना सवाल पूछें",
    placeholder="गेहूं में खाद कब डालें?"
)

# -------------------
# Ask
# -------------------
if st.button("उत्तर पाएं"):

    if query:

        prompt = f"""
        आप किसान साथी हैं।

        भारतीय किसानों को सरल भाषा में जवाब दें।

        सवाल:
        {query}

        नियम:
        - छोटा जवाब
        - हिंदी सवाल → हिंदी जवाब
        - कृषि सलाह सही हो
        """

        try:
            response = model.generate_content(prompt)

            st.success(response.text)

        except Exception as e:
            st.error(f"त्रुटि: {e}")

    else:
        st.warning("कृपया सवाल लिखें")
