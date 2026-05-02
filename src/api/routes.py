import os
import shutil
import re
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse

from src.agents.content_extractor import ContentExtractor
from src.agents.summarizer import Summarizer
from src.agents.slide_generator import SlideGenerator

router = APIRouter()

# 📁 Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "../../uploads")
OUTPUT_DIR = os.path.join(BASE_DIR, "../../output")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)



@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        print("Received file:", file.filename)

        if not file.filename:
            return {"error": "No file uploaded"}

        import re
        safe_filename = re.sub(r"[^a-zA-Z0-9_.-]", "_", file.filename)

        file_path = os.path.join(UPLOAD_DIR, safe_filename)

        print("Saving to:", file_path)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print("File saved successfully")

        return {
            "message": "File uploaded successfully",
            "filename": safe_filename
        }

    except Exception as e:
        print("UPLOAD ERROR:", e)
        return {"error": str(e)}



@router.get("/generate/")
async def generate_presentation():
    try:
        extractor = ContentExtractor(directory=UPLOAD_DIR)
        extracted_content = extractor.extract_from_directory()

        summarizer = Summarizer()
        slide_generator = SlideGenerator(output_dir="output/")

        all_slides = []

        for filename, text in extracted_content.items():
            summary = summarizer.summarize_text(text)

            summary_points = [
                p.strip() for p in summary.split("\n") if p.strip()
            ]

            all_slides.append({
                "title": filename,
                "type": "content",
                "content": summary_points[:5]
            })

        
        slide_generator.generate_presentation(all_slides)

        return {
            "message": "Slides generated",
            "download_url": "/download/?filename=output/generated_presentation.pptx"
        }

    except Exception as e:
        print("GENERATE ERROR:", e)
        return {"error": str(e)}



@router.get("/download/")
async def download_presentation(filename: str):
    return FileResponse(
        path=filename,
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        filename="AI_Presentation.pptx"
    )
