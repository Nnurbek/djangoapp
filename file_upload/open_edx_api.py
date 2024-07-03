 
import requests
from django.conf import settings

def get_access_token():
    url = f"{settings.OPEN_EDX_API_URL}/oauth2/access_token/"
    data = {
        'grant_type': 'password',
        'username': settings.OPEN_EDX_USERNAME,
        'password': settings.OPEN_EDX_PASSWORD,
        'client_id': settings.OPEN_EDX_CLIENT_ID,
        'client_secret': settings.OPEN_EDX_CLIENT_SECRET,
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()['access_token']

def get_courses():
    token = get_access_token()
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(f"{settings.OPEN_EDX_API_URL}/api/courses/v1/courses/", headers=headers)
    response.raise_for_status()
    return response.json()
