''' Script to test the API '''
import requests


add_competitor_URL = "http://127.0.0.1:8000/new-competitor"

data = {
  "first_name": "Nikos",
  "last_name": "Kyriakopoulos",
  "rating": 1000.0,
}
add_competitor_response = requests.post(add_competitor_URL, json=data)

print(add_competitor_response.status_code)
print(add_competitor_response.text)
