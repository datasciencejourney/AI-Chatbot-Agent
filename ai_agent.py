from dotenv import load_dotenv
import os

load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# LLMs
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

# Tool
from langchain_tavily import TavilySearch

# Agent (CORRECT)
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):

    # ✅ FIX provider case
    provider = provider.lower()

    # ✅ Initialize LLM properly
    if provider == "groq":
        llm = ChatGroq(
            model=llm_id,
            api_key=GROQ_API_KEY
        )
    elif provider == "openai":
        llm = ChatOpenAI(
            model=llm_id,
            api_key=OPENAI_API_KEY
        )
    else:
        return "Invalid provider"

    # ✅ Tools
    tools = [TavilySearch(max_results=2)] if allow_search else []

    # ✅ Correct agent
    agent = create_react_agent(
        llm,
        tools=tools
    )

    # ✅ Invoke
    response = agent.invoke({
        "messages": [
            {"role": "system", "content": system_prompt},   # ✅ add here
            {"role": "user", "content": query}
        ]
    })

    # ✅ Extract response safely
    messages = response.get("messages", [])
    ai_messages = [
        msg.content for msg in messages if isinstance(msg, AIMessage)
    ]

    return ai_messages[-1] if ai_messages else "No response generated."