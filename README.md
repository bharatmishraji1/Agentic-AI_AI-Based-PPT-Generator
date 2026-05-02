# 🤖 Agentic AI: Automated PPT Generator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/OpenRouter-FF6B6B?style=for-the-badge&logo=openai&logoColor=white" alt="OpenRouter">
</p>

<p align="center">
  Transform static documents into professional presentations in seconds with this end-to-end Agentic AI system.
</p>

---

## 🌟 Overview

Manual slide creation is often a bottleneck in productivity. This project leverages Agentic AI and Large Language Models (LLMs) to handle the heavy lifting. By breaking the process into specialized, modular agents, the system ensures high-quality summarization and logical slide flow.

### The Workflow:
- **Upload**: Drop your PDF, DOCX, CSV, or TXT file.
- **Process**: AI agents extract, summarize, and structure the data.
- **Download**: Get a polished `.pptx` file ready for your meeting.

---

## ✨ Features

- 📂 **Multi-Format Support**: Seamlessly handles PDF, DOCX, CSV, and TXT files.
- 🧠 **Intelligent Agents**: A modular pipeline consisting of specialized agents:
  - **Content Extractor**: Parses raw data without loss of context.
  - **Summarizer Agent**: Distills complex information into key bullet points.
  - **Slide Generator Agent**: Maps summaries into a logical presentation hierarchy.
- 🎨 **Gamma-Inspired UI**: A modern, sleek interface built with Streamlit.
- ⚡ **High-Performance Backend**: Powered by FastAPI for rapid request handling.
- 🔁 **Robust Fallback System**: Automatic model switching via OpenRouter to ensure 100% uptime.

---

## 🏗️ Tech Stack

| Component      | Technology                          |
|----------------|-------------------------------------|
| Backend        | FastAPI, Uvicorn                    |
| Frontend       | Streamlit                           |
| AI Models      | OpenRouter (Access to various LLMs) |
| File Processing| PyMuPDF, python-docx, pandas        |
| PPT Generation | python-pptx                         |

---

## ⚙️ How It Works

1. **Extraction**: The system reads the uploaded file using domain-specific libraries.
2. **Summarization**: The LLM identifies the core narrative and supporting details.
3. **Structuring**: Content is divided into Title, Introduction, Body Slides, and Conclusion.
4. **Generation**: The `python-pptx` engine builds the slides programmatically.

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Agentic-AI_AI-Based-PPT-Generator

cd Agentic-AI_AI-Based-PPT-Generator

```

### 2. Set Up Environment
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure Keys
Create a `.env` file in the root directory:
```bash
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ Running the Project

### Start the Backend (FastAPI)
```bash
uvicorn src.api.main:app --reload
```
Access API Docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Start the Frontend (Streamlit)
```bash
streamlit run app.py
```

---

## 🛠️ Challenges & Solutions

- **File Persistence**: Resolved SpooledTemporaryFile issues by implementing `shutil.copyfileobj()` to ensure stable file handling.
- **Model Reliability**: Overcame API limitations by integrating OpenRouter, allowing the system to use free-tier models with custom fallback logic.
- **Architecture Bloat**: Simplified the system by removing LlamaIndex in favor of a custom, lightweight agent-based design to reduce latency.

---

## 🔮 Future Roadmap

- [ ] AI Image Generation: Automatically generate relevant DALL-E/Midjourney images for slide backgrounds.
- [ ] Live Preview: Edit slide content directly in the UI before downloading.
- [ ] Advanced Templates: Add custom branding and professional themes.
- [ ] Cloud Integration: Deploy via AWS/GCP for global access.

---

## 👤 Author

**Bharat Mishra**  
AI/ML Developer & Data Scientist  
National Finalist (Top 2%) - India AI Impact Buildathon 2026

If you find this project useful, please consider giving it a ⭐ on GitHub!

---

<p align="center">
  <img src="https://via.placeholder.com/800x400.png?text=Demo+Screenshot" alt="Demo Screenshot" width="600">
</p>
