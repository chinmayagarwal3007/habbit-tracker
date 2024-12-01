import requests
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = 'https://pixe.la/v1/users'

usernametest = os.getenv("usernametest")
token = os.getenv("token")


user_params = {
    "token":token,
    "username":usernametest,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{usernametest}/graphs"

headers = {
    "X-USER-TOKEN": token
}

graphid = "graph1"

graphs_param = {
    "id": graphid,
    "name": "test graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

#response = requests.post(url=graph_endpoint, json=graphs_param, headers=headers)


data_endpoint = f"{graph_endpoint}/{graphid}"

data_params = {
    "date":"20241130",
    "quantity":"10",
}

response = requests.post(url=data_endpoint, json=data_params, headers = headers)
print(response.text)


