from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile


app = FastAPI()


# ============================================================
# UPLOAD DIRECTORY
# ============================================================

UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(
    exist_ok=True
)


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Lesson 9 - File Upload"
    }


# ============================================================
# UPLOAD FILE
# POST /upload
# ============================================================

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:

        while chunk := await file.read(1024 * 1024):

            buffer.write(chunk)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file_path.stat().st_size
    }


# ============================================================
# GET ALL FILES
# GET /files
# ============================================================

@app.get("/files")
def get_files():

    files = []

    for file in UPLOAD_DIR.iterdir():

        if file.is_file():

            files.append({
                "filename": file.name,
                "size": file.stat().st_size
            })

    return {
        "count": len(files),
        "files": files
    }


# ============================================================
# GET FILE INFORMATION
# GET /files/{filename}
# ============================================================

@app.get("/files/{filename}")
def get_file_info(
    filename: str
):

    file_path = UPLOAD_DIR / filename

    if not file_path.exists():

        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return {
        "filename": filename,
        "size": file_path.stat().st_size
    }