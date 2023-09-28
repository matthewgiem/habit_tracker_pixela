import requests
from tokens import TOKEN, USERNAME, GRAPHID

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = USERNAME
TOKEN = TOKEN

header = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": GRAPHID,
    "name": "reading",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"

}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


def create_new_user():
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)

def create_graph():
    response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
    print(response.text)

create_graph()