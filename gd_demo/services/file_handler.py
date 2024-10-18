import io
import os
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload, MediaInMemoryUpload
from fastapi import UploadFile, File
from accessors import gd_service, gd_credentials
from common.constants import default_file_list_fields
from common.log import default_logger
from common import utils

logger = default_logger(__name__)


def list_files(page_size=10):
    """
    Develop functionality to list all files in the user’s Google Drive.
    Display file names, types, and last modified dates.
    :param page_size:
    :return:
    """
    creds = gd_credentials.get_credentials()
    drive = gd_service.get_gd_service(credentials=creds)
    results = (drive.files().list(pageSize=page_size, fields=default_file_list_fields).execute())
    items = results.get("files", [])
    if not items:
        logger.debug("No files found.")
        return []
    return items


def upload_file(local_file_path: str):
    """
    Implement a feature to upload a file to the user’s Google Drive.
    Allow the user to select a file from their local system and upload it
    to a specified folder in Google Drive.
    :param local_file_path:
    :return:
    """
    creds = gd_credentials.get_credentials()
    drive_service = gd_service.get_gd_service(credentials=creds)
    file_name = local_file_path.split(os.path.sep)[-1]
    file_metadata = {
        'name': file_name
        # 'parents': ['<folder_id>']  # ID of the folder where you want to upload
    }
    # for image: mimetype="image/jpeg"
    media = MediaFileUpload(local_file_path, mimetype='text/plain')
    # this may throw HttpError
    response = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return response.get('id')


def upload_file_from_fastapi(uploaded_file: UploadFile = File(...)):
    creds = gd_credentials.get_credentials()
    drive_service = gd_service.get_gd_service(credentials=creds)
    file_name = uploaded_file.filename
    tmp_path = utils.save_upload_file_tmp(uploaded_file)
    file_metadata = {
        'name': file_name
        # 'parents': ['<folder_id>']  # ID of the folder where you want to upload
    }
    media = MediaFileUpload(tmp_path, mimetype=uploaded_file.content_type)
    response = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    tmp_path.unlink()
    return response.get('id')


def create_google_drive_folder(google_drive_folder_name: str):
    creds = gd_credentials.get_credentials()
    drive_service = gd_service.get_gd_service(credentials=creds)
    folder_metadata = {
        'name': google_drive_folder_name,
        # 'parents': ['<parent_folder_id>']  # ID of the parent folder (optional)
    }
    folder = drive_service.files().create(body=folder_metadata, fields='id').execute()
    logger.debug(f"created folder response: {folder}")


def download_file_by_id(file_id: str, local_save_path: str):
    """
    Implement a feature to download a file from the user’s Google Drive.
    Allow the user to select a file from the list of files and download it
    to their local system.
    :param file_id: google drive file_id, which is returned from list_files
    :param local_save_path: path to store downloaded file locally
    :return:
    """
    creds = gd_credentials.get_credentials()
    drive_service = gd_service.get_gd_service(credentials=creds)
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.FileIO(local_save_path, mode='wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False

    while not done:
        status, done = downloader.next_chunk()


def delete_file(file_id: str):
    """
    Implement a feature to delete a file from the user’s Google Drive.
    Allow the user to select a file from the list of files and delete it.
    :param file_id: google drive file id
    :return:
    """
    if not file_id:
        return None
    creds = gd_credentials.get_credentials()
    drive_service = gd_service.get_gd_service(credentials=creds)
    response = drive_service.files().delete(fileId=file_id).execute()
    return response


def delete_file_using_trash(file_id: str):
    """
    :param file_id: google drive file id
    :return:
    """
    if not file_id:
        return None
    creds = gd_credentials.get_credentials()
    drive_service = gd_service.get_gd_service(credentials=creds)
    body_value = {'trashed': True}
    response1 = drive_service.files().update(fileId=file_id, body=body_value).execute()
    response2 = drive_service.files().emptyTrash().execute()
    return response1, response2
