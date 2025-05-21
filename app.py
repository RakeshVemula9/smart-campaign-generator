# Smart Campaign Generator using OpenRouter (Mixtral)

import streamlit as st
import requests
import os

# Page config
st.set_page_config(page_title="🎯 Smart Campaign Generator", layout="centered")
st.title("🎯 Smart Campaign Generator")

# Sidebar for input
with st.sidebar:
    st.header("📝 Campaign Settings")
    product_name = st.text_input("Product Name", "Xeno CRM")
    audience = st.text_input("Target Audience", "Retail Store Owners")
    goal = st.selectbox("Campaign Goal", ["Increase Sales", "Product Awareness", "Upsell", "Launch Event"])
    tone = st.selectbox("Tone", ["Friendly", "Emotional", "Professional", "Playful"])
    channel = st.selectbox("Delivery Channel", ["Email", "SMS", "WhatsApp"])
    call_to_action = st.text_input("Call To Action", "Start Free Trial")

# OpenRouter API config
OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"] if "OPENROUTER_API_KEY" in st.secrets else st.text_input("🔑 Enter your OpenRouter API Key", type="password")
model = "mistralai/mixtral-8x7b"

# Prompt builder
def generate_prompt():
    return f"""
Act as a marketing expert.
Generate a {channel} campaign for the following:
Product: {product_name}
Audience: {audience}
Goal: {goal}
Tone: {tone}
Call to Action: {call_to_action}
The campaign should be engaging, concise, and tailored for {channel.lower()}.
"""

# Generate button
if st.button("🚀 Generate Campaign"):
    if not OPENROUTER_API_KEY:
        st.warning("Please provide your OpenRouter API key.")
    else:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": "https://xeno-campaign-generator.streamlit.app",
            "X-Title": "Smart Campaign Generator"
        }
        body = {
            "model": model,
            "messages": [{"role": "user", "content": generate_prompt()}]
        }
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=body, headers=headers)

        if response.status_code == 200:
            result = response.json()
            output = result['choices'][0]['message']['content']
            st.subheader("📢 Your Campaign Copy")
            st.text_area("Generated Campaign", output, height=300)
            st.download_button("📥 Download Campaign", output, file_name="campaign.txt")
        else:
            st.error(f"Failed to generate campaign: {response.text}")

# Footer
st.markdown("""
---
Made with ❤️ using [OpenRouter](https://openrouter.ai) and Streamlit.
""")
