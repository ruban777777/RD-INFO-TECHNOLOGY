import requests
from bs4 import BeautifulSoup

# Get the web page
url = "https://www.python.org/"
response = requests.get(url)

# Parse with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract upcoming events
print("Upcoming Python Events:")
for item in soup.select(".list-recent-events li"):
    title = item.get_text(strip=True)
    print("-", title)
