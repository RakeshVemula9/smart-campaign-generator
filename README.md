# 🎯 Smart Campaign Generator

A Streamlit-powered web application that uses **OpenRouter's large language models (LLMs)** to generate, edit, and manage marketing campaigns based on your product, target audience, and campaign goals.

![Streamlit UI Screenshot](https://user-images.githubusercontent.com/placeholder.png) <!-- Optional: Replace with real screenshot -->

## 🔍 Features

- 🧠 AI-powered campaign copy generation using OpenRouter (e.g., Mixtral, Hermes)
- 📝 Editable campaign output directly in the app
- 📥 Download editable campaign text
- 🕘 Auto-saved campaign history (view last 5 versions)
- 🔒 Secure API key input (not stored permanently)

---

## 🚀 How to Run

### 🔧 Requirements

Make sure you have Python 3.8+ installed. Then:

```bash
git clone https://github.com/yourusername/smart-campaign-generator.git
cd smart-campaign-generator
pip install -r requirements.txt


### 🧪 How It Works
User enters details like product name, target audience, tone, and CTA.

The app sends a prompt to OpenRouter's API using your selected LLM model.

The model returns a tailored campaign message.

Users can edit, download, or view previously generated campaigns.
