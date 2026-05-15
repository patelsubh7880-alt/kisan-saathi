import streamlit as st
import google.generativeai as genai

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Kisan Saathi",
    page_icon="🌾",
    layout="wide"
)

# ----------------------------
# Gemini API
# ----------------------------
API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-latest")

# ----------------------------
# UI
# ----------------------------
st.title("🌾 किसान साथी")
st.subheader("कृषि सलाह सहायक | Agriculture Advisory Assistant")

st.write("फसल, खाद, सिंचाई, रोग और कीट नियंत्रण से जुड़े सवाल पूछें।")

query = st.text_input(
    "अपना सवाल पूछें / Ask your farming question",
    placeholder="जैसे: गेहूं में यूरिया कब डालें?"
)

# ----------------------------
# Ask Button
# ----------------------------
if st.button("उत्तर पाएं"):

    if query.strip():

        prompt = f"""
        आप किसान साथी हैं।

        भारतीय किसानों को सरल भाषा में कृषि सलाह दें।

        नियम:
        - जवाब छोटा और सरल हो
        - यदि सवाल हिंदी में हो तो जवाब हिंदी में दें
        - यदि सवाल अंग्रेज़ी में हो तो जवाब अंग्रेज़ी में दें
        - खाद, सिंचाई, रोग, कीट नियंत्रण पर व्यावहारिक सलाह दें
        - केवल कृषि संबंधी सही सलाह दें

        किसान का सवाल:
        {query}
        """

        try:
            response = model.generate_content(prompt)

            st.success(response.text)

        except Exception as e:
            st.error(f"त्रुटि: {e}")

    else:
        st.warning("कृपया सवाल लिखें")
