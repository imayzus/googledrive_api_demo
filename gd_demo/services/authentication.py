from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from common.exceptions import GoogleDriveDemoException
from common.constants import DEFAULT_SCOPES
from common import constants


def get_credentials_from_saved_file(auth_token: str = constants.auth_token):
    creds = Credentials.from_authorized_user_file(auth_token, DEFAULT_SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return creds


def get_initial_credentials_from_client_secrets(client_secrets_file=constants.client_secrets_file):
    flow = InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, DEFAULT_SCOPES
    )
    creds = flow.run_local_server(port=0)
    return creds


def save_credentials(creds, auth_token: str = constants.auth_token):
    with open(auth_token, "w") as token:
        token.write(creds.to_json())


def get_and_save_new_credentials(client_secrets_file=constants.client_secrets_file,
                                 auth_token: str = constants.auth_token):
    creds = get_initial_credentials_from_client_secrets(client_secrets_file)
    save_credentials(creds, auth_token=auth_token)
    return creds


def get_existing_credentials(auth_token: str = constants.auth_token):
    creds = get_credentials_from_saved_file(auth_token=auth_token)
    if not creds or not creds.valid:
        raise GoogleDriveDemoException(f"unable to get valid token from {auth_token}")
    return creds
