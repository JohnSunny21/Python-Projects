import re
import requests
from bs4 import BeautifulSoup


url = input("Enter the channel link : ")

# Headers with Accept-Language set to en-US

headers = {
    "Accept-Language": "en-US,en;q=0.9"
}

soup = BeautifulSoup(requests.get(url,headers=headers).content,"html.parser")

# print(soup.prettify())



# Use regex to find the number

match = re.search(r'"content":\s*"\b([\d.]+[MK]?)\b\s*subscribers"',soup.prettify())

if match:
    subscriber_count = match.group(1)
    print("Subscriber Count : ", subscriber_count)
else:
    print("Subscriber count not found!")