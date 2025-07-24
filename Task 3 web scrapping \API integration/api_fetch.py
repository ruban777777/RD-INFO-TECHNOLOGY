import requests

# Call API
response = requests.get("https://randomuser.me/api/")
data = response.json()

# Extract details
user = data['results'][0]
print("Name:", user['name']['first'], user['name']['last'])
print("Email:", user['email'])
print("Country:", user['location']['country'])
