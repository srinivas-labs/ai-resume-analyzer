from fastapi import FastAPI, UploadFile, File
import shutil
import os
####mycode
app = FastAPI()

UPLOAD_FOLDER = "uploads"

# Create uploads folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "AI Resume Analyzer Backend Running Successfully"}


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Resume uploaded successfully",
        "file_name": file.filename
    }