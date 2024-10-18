from services import authentication
from common.exceptions import GoogleDriveDemoException
from common import constants

cached_credentials = [None]


def get_credentials(ignore_cached=False):
    if cached_credentials[0] and not ignore_cached:
        return cached_credentials[0]
    try:
        creds = authentication.get_existing_credentials(auth_token=constants.auth_token)
    except GoogleDriveDemoException:
        creds = authentication.get_and_save_new_credentials(client_secrets_file=constants.client_secrets_file,
                                                            auth_token=constants.auth_token)
    cached_credentials[0] = creds
    return creds
