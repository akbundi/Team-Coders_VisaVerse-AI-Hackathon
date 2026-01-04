from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload")
def upload_document(doc_type: str, file: UploadFile = File(...)):
    return {
        "document": doc_type,
        "filename": file.filename,
        "status": "uploaded"
    }
