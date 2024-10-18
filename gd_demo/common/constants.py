SCOPES_READONLY = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
DEFAULT_SCOPES = ["https://www.googleapis.com/auth/drive"]

auth_token = 'token.json'
client_secrets_file = 'credentials.json'

# other possible fields="nextPageToken, files(id, name, kind, fileExtension, fullFileExtension, modifiedTime, originalFilename, description, parents, mimeType, size)"

default_file_list_fields = "nextPageToken, files(id, name, fileExtension, modifiedTime, mimeType, size, parents)"
