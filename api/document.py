from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form
from fastapi import Depends
from dependencies import get_document_service

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

@router.post("/")
def upload_document(
    name: str = Form(...),
    file: UploadFile = File(...),
    document_service = Depends(get_document_service)
):

    return document_service.ingest(
        name,
        file
    )