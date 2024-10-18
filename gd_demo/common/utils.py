import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Callable

from fastapi import UploadFile


def get_file_id_for_name(items: list, file_name: str):
    filtered = [item.get('id') for item in items if item.get('name') == file_name]
    if len(filtered) > 0:
        return filtered[0]
    return None


def generate_test_upload_file(file_name: str):
    with open(file_name, 'w') as f_out:
        for i in range(500):
            f_out.write(str(i) * 50)
            f_out.write('\n')


def get_file_content(file_name: str):
    with open(file_name, 'r') as f_in:
        content = f_in.read()
        return content


def check_files_equal(file1: str, file2: str):
    file1_content = get_file_content(file1)
    file2_content = get_file_content(file2)
    return file1_content == file2_content


def save_upload_file(upload_file: UploadFile, destination: Path) -> None:
    try:
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()


def save_upload_file_tmp(upload_file: UploadFile) -> Path:
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp_path


def handle_upload_file(
    upload_file: UploadFile, handler: Callable[[Path], None]
) -> None:
    tmp_path = save_upload_file_tmp(upload_file)
    try:
        handler(tmp_path)  # Do something with the saved temp file
    finally:
        tmp_path.unlink()  # Delete the temp file
