from fastapi import APIRouter, status, UploadFile, File
from services.file_handler import list_files, upload_file_from_fastapi, download_file_by_id, delete_file
from common.log import default_logger

logger = default_logger(__name__)

router = APIRouter()


@router.get('/list', status_code=status.HTTP_200_OK)
def list_files_view() -> list:
    items = list_files()
    return items


@router.post('/upload')
def upload_file_view(uploaded_file: UploadFile = File(...)):
    result = upload_file_from_fastapi(uploaded_file)
    return result


@router.get('/download')
def download_file_view(google_drive_file_id: str, local_save_path: str):
    result = download_file_by_id(file_id=google_drive_file_id, local_save_path=local_save_path)
    return result


@router.get('/delete')
def delete_file_view(google_drive_file_id: str):
    result = delete_file(file_id=google_drive_file_id)
    return result
