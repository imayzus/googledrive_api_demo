from googleapiclient.discovery import build


cached_gd_service = [None]


def get_gd_service(credentials, ignore_cache=False):
    if cached_gd_service[0] and not ignore_cache:
        return cached_gd_service[0]
    service = build("drive", "v3", credentials=credentials)
    cached_gd_service[0] = service
    return cached_gd_service[0]
