import streamlit as st
import os

import sys

sys.path.append(os.path.abspath("."))


from src.agents.content_extractor import ContentExtractor
from src.agents.summarizer import Summarizer
from src.agents.slide_generator import SlideGenerator

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="AI Slide Generator", layout="wide")

os.makedirs("output", exist_ok=True)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
body {
    background: #f8fafc;
}

.title {
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    font-size: 18px;
    color: #64748b;
}

.card {
    background: #eef2ff;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
}

.feature-title {
    font-weight: 600;
    margin-top: 10px;
}

.stButton>button {
    border-radius: 8px;
    padding: 10px;
    width: 100%;
}

.download-btn button {
    background: #22c55e;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.image("assets/hero2.png", width=150)
    st.markdown("## AI Slide Generator")
    st.markdown("Turn documents into presentations")

    st.markdown("---")

    st.markdown("### Features")
    st.markdown("""
- AI Summarization  
- Auto Slide Creation  
- Fast PPT Export  
""")

# =========================
# HERO SECTION
# =========================
col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/hero2.png")

with col2:
    st.markdown("<div class='title'>AI Slide Generator</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Create beautiful presentations instantly using AI</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# =========================
# MAIN CARD
# =========================
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload your file",
        type=["pdf", "docx", "csv", "txt"]
    )

    if uploaded_file:
        # Save file locally
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("File uploaded successfully")

        if st.button("⚡ Generate Slides"):

            with st.spinner("Generating slides..."):

                try:
                    # 1. Extract text
                    extractor = ContentExtractor(directory=".")
                    text = extractor.extract_from_file(file_path)

                    # 2. Summarize
                    summarizer = Summarizer()
                    summary = summarizer.summarize_text(text)

                    # 3. Convert to bullet points
                    points = [
                        p.strip() for p in summary.split("\n") if p.strip()
                    ]

                    # 4. Generate slides
                    slide_gen = SlideGenerator(output_dir="output/")

                    slides_data = [{
                        "title": "Generated Presentation",
                        "type": "content",
                        "content": points[:5]
                    }]

                    slide_gen.generate_presentation(slides_data)

                    ppt_path = "output/generated_presentation.pptx"

                    # 5. Download button
                    with open(ppt_path, "rb") as f:
                        st.download_button(
                            label="Download PPT",
                            data=f,
                            file_name="AI_Presentation.pptx"
                        )

                    st.success("Slides generated successfully!")

                except Exception as e:
                    st.error(f"Error: {str(e)}")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FEATURES SECTION
# =========================
st.write("")
st.write("")

st.markdown("## 🚀 How it works")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("assets/upload.png")
    st.markdown("<div class='feature-title'>Upload File</div>", unsafe_allow_html=True)

with col2:
    st.image("assets/processing.png")
    st.markdown("<div class='feature-title'>AI Processing</div>", unsafe_allow_html=True)

with col3:
    st.image("assets/hero.png")
    st.markdown("<div class='feature-title'>Generate Slides</div>", unsafe_allow_html=True)

with col4:
    st.image("assets/download.png")
    st.markdown("<div class='feature-title'>Download PPT</div>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<br><br>
<hr>
<p style='text-align:center;color:#64748b'>
Built by Bharat Mishra • Streamlit App 
</p>
""", unsafe_allow_html=True)
