# Smart Campaign Generator using OpenRouter (Mixtral)

import streamlit as st
import requests
import os

# Page config
st.set_page_config(page_title="🎯 Smart Campaign Generator", layout="centered")
st.title("🎯 Smart Campaign Generator")

# Session state initialization
if 'history' not in st.session_state:
    st.session_state.history = []
if 'editable_text' not in st.session_state:
    st.session_state.editable_text = ""

# Sidebar for input
with st.sidebar:
    st.header("📝 Campaign Settings")
    product_name = st.text_input("Product Name", "Xeno CRM")
    audience = st.text_input("Target Audience", "Retail Store Owners")
    goal = st.selectbox("Campaign Goal", ["Increase Sales", "Product Awareness", "Upsell", "Launch Event"])
    tone = st.selectbox("Tone", ["Friendly", "Emotional", "Professional", "Playful"])
    channel = st.selectbox("Delivery Channel", ["Email", "SMS", "WhatsApp"])
    call_to_action = st.text_input("Call To Action", "Start Free Trial")
    model = st.selectbox("Choose LLM Model", [
        "mistralai/mixtral-8x7b-instruct",
        "nousresearch/nous-hermes-2-mixtral"
    ])

# OpenRouter API config
OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"] if "OPENROUTER_API_KEY" in st.secrets else st.text_input("🔑 Enter your OpenRouter API Key", type="password")

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

        try:
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=body, headers=headers)
            response.raise_for_status()
            result = response.json()
            output = result['choices'][0]['message']['content']

            # Save to history and session state
            st.session_state.history.append(output)
            st.session_state.editable_text = output

        except requests.exceptions.HTTPError as http_err:
            st.error(f"HTTP error occurred: {http_err}\nResponse: {response.text}")
        except Exception as err:
            st.error(f"An error occurred: {err}")

# Editable campaign
if st.session_state.editable_text:
    st.subheader("✏️ Edit Your Campaign")
    edited = st.text_area("Edit Campaign Text", st.session_state.editable_text, height=300)
    st.download_button("📥 Download Edited Campaign", edited, file_name="edited_campaign.txt")

# History section
if st.session_state.history:
    with st.expander("📜 View Campaign History"):
        for i, past in enumerate(reversed(st.session_state.history[-5:]), 1):
            st.markdown(f"**Version {len(st.session_state.history) - i + 1}:**\n\n{past}")

# Footer
st.markdown("""
---
Made with ❤️ using [OpenRouter](https://openrouter.ai) and Streamlit.
""")
