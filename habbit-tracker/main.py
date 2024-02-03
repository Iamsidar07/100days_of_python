import requests
from datetime import datetime

USERNAME = "iamsidar07"
SECRET = "aB3#dEfgHijklmnopQR$56789stuvwxyZ"
GRAPH_ID = "graph-1"

BASE_URL = "https://pixe.la/v1/users"

# Create user
user_data = {
    "token": SECRET,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=BASE_URL, json=user_data)
# response.raise_for_status()
# print("create user: ", response.text)

# Create graph
headers = {
    "X-USER-TOKEN": SECRET
}

graph_data = {
    "id": GRAPH_ID,
    "name": "Code Club",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}

# response = requests.post(url=f"{BASE_URL}/{USERNAME}/graphs", json=graph_data, headers=headers)
# response.raise_for_status()
# print("graph",response.text)

today = datetime.now().strftime("%Y%m%d")
# post value to the graph
post_value_data = {
    "date": today, 
    "quantity": input("How many commits? ")
}

response = requests.post(
    url=f"{BASE_URL}/{USERNAME}/graphs/{GRAPH_ID}",
    json=post_value_data,
    headers=headers,
)
response.raise_for_status()
print("streak", response.text)

new_pixel_data = {"quantity": "1"}
# response = requests.put(
#     url=f"{BASE_URL}/{USERNAME}/graphs/{GRAPH_ID}/{today}",
#       json=new_pixel_data, 
#       headers=headers
# )
# response.raise_for_status()
# print(response.text)

# response = requests.delete(
#     url=f"{BASE_URL}/{USERNAME}/graphs/{GRAPH_ID}/{today}",  
#     headers=headers
# )
# response.raise_for_status()
# print(response.text)
