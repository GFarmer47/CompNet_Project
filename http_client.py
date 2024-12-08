import requests

url = 'http://192.168.1.103'

response = requests.get(url)
if response.status_code == 200:
    print("Server response:")
    print(response.text)
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
