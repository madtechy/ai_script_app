import google.generativeai as genai

genai.configure(api_key="AIzaSyBfXH-dvlYsqiSbU0mwzNHpSSf4TMj3PtA")
model = genai.GenerativeModel("gemini-1.5-flash")

import streamlit as st
import google.generativeai as genai

# 1. Configure API
genai.configure(api_key="AIzaSyBfXH-dvlYsqiSbU0mwzNHpSSf4TMj3PtA")

# 2. Model
model = genai.GenerativeModel("gemini-1.5-flash")

# 3. UI
st.title("🎬 Shorts Script Generator")
topic = st.text_input("Enter a topic")
style = st.selectbox(
    "Choose Style", ["YouTube Shorts", "Funny", "Educational", "Informative"]
)

# 4. Generate Script
if st.button("Generate Script"):
    if topic:
        with st.spinner("Generating..."):
            prompt = f"Write a 60-second video script in {style} style about: {topic}"
            try:
                response = model.generate_content(prompt)
                st.subheader("📜 Your AI Script:")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter a topic to generate script.")
