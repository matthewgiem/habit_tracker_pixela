import requests
from tokens import TOKEN, USERNAME

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = USERNAME
TOKEN = TOKEN

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


def create_new_user():
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)
