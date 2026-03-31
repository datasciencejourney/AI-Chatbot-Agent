# Setup UI with streamlit
import streamlit as st
import requests

st.set_page_config(page_title="LangGraph AI Agent", layout="centered")
st.title("AI Chatbot Agent")
st.write("Interact with the AI Agent powered by LangGraph and search tools.")

system_prompt = st.text_area(
    "Define your AI Agent: ", height=150, placeholder="Type your prompt here...")

MODEL_NAMES_GROQ = ["openai/gpt-oss-20b", "llama-3.3-70b-versatile"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select AI Model Provider:", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select AI Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select AI Model:", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search", value=False)

user_query = st.text_area("Your Message: ", height=150,
                          placeholder="Type your message here...")

API_URL = "http://127.0.0.1:8000/chat"

if st.button("Ask Agent"):
    if user_query.strip():
        # connect with backend via URL
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response = requests.post(API_URL, json=payload)

        st.write("Status Code:", response.status_code)
        #st.write("Raw Response:", response.text)  # 🔥 debugging

        if response.status_code == 200:
            data = response.json()

            if "error" in data:
                st.error(data["error"])
            else:
                st.subheader("AI Agent Response:")
                st.markdown(f"**Final response:** {data.get('response', data)}")

        else:
            st.error(f"Request failed with status code {response.status_code}")
# connect with backend via URL
