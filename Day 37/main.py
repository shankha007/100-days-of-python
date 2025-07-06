import requests
import env
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "shankhad007"

## To create a Pixela User

# user_params = {
#     "token": env.PIXELA_TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

## Done: Pixela Profile Page: https://pixe.la/@shankhad007

## Create a graph - Cycling Graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

graph_headers = {
    "X-USER-TOKEN": env.PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers)
# print(response.text)

## Creating a entry into the Graph

cycling_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
random_date = datetime(year=2025, month=7, day=5)

cycling_graph_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8.19"
}

# response = requests.post(url=cycling_graph_endpoint, headers=graph_headers, json=cycling_graph_params)
# print(response.text)

## Update a Pixel

pixel_update_endpoint = f"{cycling_graph_endpoint}/20250705"

updated_params = {
    "quantity": "7.23"
}

# response = requests.put(url=pixel_update_endpoint, headers=graph_headers, json=updated_params)
# print(response.text)

## Delete a Pixel

pixel_delete_endpoint = f"{cycling_graph_endpoint}/20250705"

response = requests.delete(url=pixel_delete_endpoint, headers=graph_headers)
print(response.text)
