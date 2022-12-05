import requests
import datetime

USERNAME = "b34ux"
TOKEN = "supersecretpassword"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN, 
    "username": USERNAME, 
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"
}

# Comment out in order to continue exercise - User now created.
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",

}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Comment out in order to continue exercise - Graph now created.
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.71",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)