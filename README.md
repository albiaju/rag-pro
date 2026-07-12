# 📝 Build Your Local RAG System with LLMs

Welcome to the **Local LLM-based Retrieval-Augmented Generation (RAG) System**! This repository provides the full code to build a private, offline RAG system for managing and querying personal documents locally using a combination of OpenSearch, Sentence Transformers, and Large Language Models (LLMs). Perfect for anyone seeking a privacy-friendly solution to manage documents without relying on cloud services.

![Demo Image](images/chatbot.png)

### 🌟 Key Features:
- **Privacy-Friendly Document Search:** Search through personal documents without uploading them to the cloud.
- **Hybrid Search with OpenSearch:** Uses both traditional text matching and semantic search.
- **Easy Integration with LLMs**: Leverage local LLMs for personalized, context-aware responses.

### 🚀 Get Started
1. Clone the repo: `git clone https://github.com/JAMwithAI/build_your_local_RAG_system.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure `constants.py` for embedding models and OpenSearch settings.
4. Run the Streamlit app: `streamlit run welcome.py`

### � Deploy on Render
This project can be deployed on Render using the included `Dockerfile` and `render.yaml`.

Render deployment notes:
- Set `PORT=8501` (default).
- Set `OPENSEARCH_HOST` and `OPENSEARCH_PORT` to your OpenSearch service.
- Set `OLLAMA_ADDRESS` to your Ollama daemon address (for example `http://localhost:11434` or a remote host).
- Set `OLLAMA_MODEL_NAME` if you want a different Ollama model.

To deploy on Render:
1. Push this repo to GitHub.
2. Add a new Web Service in Render and choose Docker.
3. Use `Dockerfile` from this repository.
4. Configure the required environment variables in Render.

> Note: This app requires access to an OpenSearch instance and an Ollama service. Render hosts the Streamlit app, but those backend services must be reachable from the deployed service.

### �📘 Blog Guide
For a detailed walkthrough of the setup and code, check out our blog:

[**Build a Local LLM-based RAG System for Your Personal Documents - Part 1**](https://jamwithai.substack.com/p/build-a-local-llm-based-rag-system)

[**Build a Local LLM-based RAG System for Your Personal Documents - Part 2: The Guide**](https://jamwithai.substack.com/p/build-a-local-llm-based-rag-system-628)

---

Enjoy your journey in building a private, AI-driven document management system! If you find this project useful, consider sharing it with others in the community!
