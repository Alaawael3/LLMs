# 🧠 Ask My Company’s Chatbot

A conversational AI chatbot built with [LangChain](https://www.langchain.com/), [Gemini 1.5 Pro](https://ai.google.dev/), FAISS vector search, and [Streamlit](https://streamlit.io/) to intelligently answer company-specific FAQs. The model answers questions based solely on a provided CSV knowledge base and avoids hallucinations by responding with "I don't know" when context is insufficient.

---

## 🚀 Features

- 🔎 **Vector Search (FAISS)**: Semantic search on your company's FAQ data.
- 🤖 **LLM Integration (Gemini 1.5 Pro)**: Accurate and context-aware responses.
- 📁 **CSV Knowledge Base**: Easily update your source documents by modifying `codebasics_faqs.csv`.
- 🔗 **LangChain-Powered Chains**: Prompt templating and document-based QA.
- 🖥️ **Streamlit Frontend**: Simple and interactive web UI.

---

## 🧩 Tech Stack

- `LangChain`
- `Gemini 1.5 Pro` via `langchain-google-genai`
- `FAISS` (local vector storage)
- `HuggingFace Embeddings` (`all-MiniLM-L6-v2`)
- `Streamlit` (for web interface)
- `dotenv` for API key management

---