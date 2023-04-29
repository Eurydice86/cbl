''' Script to test the API '''
import requests


add_competitor_URL = "http://127.0.0.1:8000/competitors"

data = {
  "first_name": "iita",
  "last_name": "Lehtinen",
}
add_competitor_response = requests.post(add_competitor_URL, json=data)

print(add_competitor_response.status_code)
print(add_competitor_response.text)
