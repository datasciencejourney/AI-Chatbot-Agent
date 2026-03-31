# 🤖 AI Chatbot Agent (LLM + FastAPI + Tool Calling)

An intelligent, production-ready AI chatbot agent built using Large Language Models (LLMs) with tool-calling capabilities. This project demonstrates real-world applications of LLMs including reasoning, web search, and modular agent design.

---

## 🌟 Why this project stands out

- ✅ Built using **Agent-based architecture (ReAct paradigm)**
- ✅ Integrates **LLMs + external tools (Tavily Search)**
- ✅ Designed like a **real production backend (FastAPI)**
- ✅ Clean, scalable, and modular codebase
- ✅ Demonstrates **applied AI engineering skills** (not just theory)

---

## 🎥 Demo

### 🔹 Chatbot Interaction

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/818bc056-141f-4bbc-aae8-b6e0bfb6aaa8" />


---

### Flow:
1. User sends query → FastAPI endpoint  
2. Query passed to LLM Agent  
3. Agent decides:
   - Answer directly OR
   - Call external tool (Tavily Search)  
4. Tool returns data  
5. LLM generates final response  
6. Response sent back to user  

---

## 🛠️ Tech Stack

| Category        | Tools Used |
|----------------|-----------|
| Backend        | FastAPI |
| LLMs           | OpenAI / Groq |
| Agent Framework| LangChain |
| Search Tool    | Tavily API |
| Language       | Python |

---

## 📁 Project Structure


agentic-chatbot-FastAPI/
│── main.py # FastAPI app
│── ai-agent.py # Agent logic
│── requirements.txt
│── .env # API keys (ignored)
│── .gitignore
│── assets/ # Screenshots & diagrams
│── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/datasciencejourney/AI-Chatbot-Agent.git
cd AI-Chatbot-Agent
2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables

Create a .env file:

OPENAI_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
5. Run the application
uvicorn main:app --reload
📡 API Endpoint
POST /chat

Request:

{
  "query": "What are the latest AI trends?"
}

Response:

{
  "response": "AI is evolving rapidly with advancements in..."
}
🧪 Example Use Cases
🔹 AI-powered assistant
🔹 Research automation
🔹 Real-time web-augmented Q&A
🔹 Backend for AI SaaS products
🔐 Security Best Practices
API keys stored securely in .env
.env excluded via .gitignore
No secrets exposed in codebase
🚀 Future Improvements
🔹 Add frontend (React / Streamlit)
🔹 Conversation memory (RAG / vector DB)
🔹 Multi-agent workflows
🔹 Deployment (AWS / GCP / Docker)
👤 Author

datasciencejourney

⭐ If you found this useful

Give it a ⭐ and feel free to contribute!
