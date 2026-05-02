import streamlit as st
import requests

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="AI Slide Generator", layout="wide")

API_BASE = "http://127.0.0.1:8000"

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

.primary-btn button {
    background: #1e293b;
    color: white;
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
# UPLOAD + GENERATE CARD
# =========================
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload your file",
        type=["pdf", "docx", "csv", "txt"]
    )

    if st.button("Upload File"):
        if uploaded_file:
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
            res = requests.post(f"{API_BASE}/upload/", files=files)

            if res.status_code == 200:
                st.success("Uploaded successfully")
            else:
                st.error("Upload failed")
        else:
            st.warning("Please select a file")

    if st.button("⚡ Generate Slides"):
        with st.spinner("Generating slides..."):
            res = requests.get(f"{API_BASE}/generate/")
            data = res.json()

            if "download_url" in data:
                st.success("Slides generated!")

                st.markdown(f"""
                <a href="{API_BASE}{data['download_url']}" target="_blank">
                    <button style="
                        background:#22c55e;
                        color:white;
                        padding:10px 20px;
                        border:none;
                        border-radius:8px;
                        width:100%;
                    ">
                         Download PPT
                    </button>
                </a>
                """, unsafe_allow_html=True)
            else:
                st.error(data.get("error", "Error"))

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FEATURES SECTION
# =========================
st.write("")
st.write("")

st.markdown("## How it works")

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
Built with AI • Streamlit App
</p>
""", unsafe_allow_html=True)
