import requests
from tokens import TOKEN, USERNAME, GRAPHID
from datetime import date

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


pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pages_read_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"


def create_new_user():
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


def create_graph():
    response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
    print(response.text)


def add_pages_read(num):
    today = date.today()
    add_pages = {
        "date": f"{today.year}{today.month:02d}{today.day:02d}",
        "quantity": str(num)
    }
    response = requests.post(url=pages_read_endpoint, json=add_pages, headers=header)
    print(response.text)


def update_todays_pages_read(num):
    today = date.today()
    change_pages = {
        "quantity": str(num)
    }
    update_url = pages_read_endpoint + f"/{today.year}{today.month:02d}{today.day:02d}"
    response = requests.put(url=update_url, json=change_pages, headers=header)
    print(response.text)


def update_pages_read(num, change_date):
    change_pages = {
        "quantity": str(num)
    }
    update_url = pages_read_endpoint + f"/{change_date}"
    response = requests.put(url=update_url, json=change_pages, headers=header)
    print(response.text)


def delete_pixel(delete_date):
    delete_url = pages_read_endpoint + f"/{delete_date}"
    response = requests.delete(url=delete_url, headers=header)
    print(response.text)

