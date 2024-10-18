from services.authentication import get_and_save_new_credentials, get_existing_credentials


def test_get_new_credentials():
    get_and_save_new_credentials()


def test_get_existing_credentials():
    get_existing_credentials()

