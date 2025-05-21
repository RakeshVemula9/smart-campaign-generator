import streamlit as st
from openai import OpenAI
import os

# Get API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Smart Campaign Generator", page_icon="📣")

st.title("📣 Smart Campaign Generator")
st.markdown("Create AI-powered marketing campaigns using GPT!")

# Input fields
product = st.text_input("🛍️ Product Name", placeholder="e.g. Organic Face Cream")
audience = st.text_input("🎯 Target Audience", placeholder="e.g. Women aged 20-35")
tone = st.selectbox("🎨 Tone of Message", ["Friendly", "Professional", "Excited", "Urgent"])

# Generate button
if st.button("Generate Campaign") and product and audience:
    prompt = (
        f"Generate a {tone.lower()} marketing campaign message for the following:\n"
        f"Product: {product}\n"
        f"Target Audience: {audience}\n"
        f"Make it short, engaging, and suitable for email or SMS."
    )

    with st.spinner("Generating campaign..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a marketing expert."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.7
            )
            message = response.choices[0].message.content
            st.success("✅ Campaign Generated!")
            st.text_area("📄 Campaign Text", value=message, height=200)
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.info("Please fill out all fields and click 'Generate Campaign'.")
