import streamlit as st
import requests
import os

# Load Hugging Face API token from Streamlit secrets or environment variables
HF_API_TOKEN = st.secrets.get("HF_API_TOKEN") or os.getenv("HF_API_TOKEN")

st.set_page_config(page_title="Smart Campaign Generator", page_icon="📣")
st.title("📣 Smart Campaign Generator")
st.markdown("Create AI-powered marketing campaigns using Hugging Face!")

# Input fields
product = st.text_input("🛍️ Product Name", placeholder="e.g. Organic Face Cream")
audience = st.text_input("🎯 Target Audience", placeholder="e.g. Women aged 20-35")
tone = st.selectbox("🎨 Tone of Message", ["Friendly", "Professional", "Excited", "Urgent"])

def generate_campaign(prompt):
    API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
  # You can replace this with a bigger model if you want
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 100, "temperature": 0.7}}

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        # The result is usually a list of dicts with 'generated_text' key
        return data[0]['generated_text']
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

if st.button("Generate Campaign") and product and audience:
    prompt = (
        f"Generate a {tone.lower()} marketing campaign message for the following:\n"
        f"Product: {product}\n"
        f"Target Audience: {audience}\n"
        f"Make it short, engaging, and suitable for email or SMS."
    )
    with st.spinner("Generating campaign..."):
        try:
            campaign_text = generate_campaign(prompt)
            st.success("✅ Campaign Generated!")
            st.text_area("📄 Campaign Text", value=campaign_text, height=200)
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.info("Please fill out all fields and click 'Generate Campaign'.")
