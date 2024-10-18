from services.file_handler import list_files, upload_file, download_file_by_id, delete_file
from common.utils import get_file_id_for_name, generate_test_upload_file, check_files_equal
from common.log import default_logger

logger = default_logger(__name__)


def test_upload_file():
    fname = 'integration_tests/test_data/test_file.txt'
    generate_test_upload_file(file_name=fname)
    result = upload_file(fname)
    logger.info(f"uploaded file ID: {result}")
    assert bool(result)


def test_list_files():
    items = list_files()
    fname = "test_file.txt"
    file_id = get_file_id_for_name(items=items, file_name=fname)
    assert file_id is not None, f"file id for {fname} not found from list_files"


def test_download_file():
    fname = "test_file.txt"
    items = list_files()
    file_id = get_file_id_for_name(items=items, file_name=fname)
    assert file_id is not None
    local_save_path = 'integration_tests/test_data/downloaded_test_file.txt'
    download_file_by_id(file_id=file_id, local_save_path=local_save_path)
    original_file = 'integration_tests/test_data/test_file.txt'
    result = check_files_equal(local_save_path, original_file)
    assert result


def test_delete_file():
    fname = "test_file.txt"
    items = list_files()
    file_id = get_file_id_for_name(items=items, file_name=fname)
    assert file_id is not None
    response = delete_file(file_id=file_id)
    logger.debug(f"deleted file response: {response}")
    items = list_files()
    file_id = get_file_id_for_name(items=items, file_name=fname)
    assert file_id is None
