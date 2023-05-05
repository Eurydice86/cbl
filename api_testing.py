''' Script to test the API '''
import requests


add_competitor_URL = "http://127.0.0.1:8000/competitors"

data = {
  "first_name": "iita",
  "last_name": "Lehtinen",
}
#add_competitor_response = requests.post(add_competitor_URL, json=data)

#print(add_competitor_response.status_code)
#print(add_competitor_response.text)


new_fight_URL = "http://127.0.0.1:8000/new_fight"

data = {
  "winner_uid": "0684b247ba5a4eea9bea958562242de6",
  "loser_uid": "758498fdedf74f4aaf0b554212e9fd88",
}
new_fight_response = requests.post(new_fight_URL, json=data)

print(new_fight_response.status_code)
print(new_fight_response.text)
