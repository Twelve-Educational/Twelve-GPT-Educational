import streamlit as st

GPT_BASE = st.secrets.get("GPT_BASE")
GPT_VERSION = st.secrets.get("GPT_VERSION")
GPT_KEY = st.secrets.get("GPT_KEY")
GPT_CHAT_MODEL = st.secrets.get("GPT_CHAT_MODEL")
GPT_EMBEDDINGS_MODEL = st.secrets.get("GPT_EMBEDDINGS_MODEL")

# Gemini secrets
USE_GEMINI = st.secrets.get("USE_GEMINI", False)
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", "")
GEMINI_CHAT_MODEL = st.secrets.get("GEMINI_CHAT_MODEL", "")
GEMINI_EMBEDDING_MODEL = st.secrets.get("GEMINI_EMBEDDING_MODEL", "")
