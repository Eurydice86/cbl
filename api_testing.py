''' Script to test the API '''
import requests


ADD_COMPETITOR_URL = "http://127.0.0.1:8000/competitors"

data = {
  "first_name": "Nikos",
  "last_name": "Kyriakopoulos",
}
add_competitor_response = requests.post(ADD_COMPETITOR_URL, json=data)

print(add_competitor_response.status_code)
print(add_competitor_response.text)


#NEW_FIGHT_URL = "http://127.0.0.1:8000/new_fight"

#data = {
#  "winner_uid": "0684b247ba5a4eea9bea958562242de6",
#  "loser_uid": "758498fdedf74f4aaf0b554212e9fd88",
#}
#new_fight_response = requests.post(NEW_FIGHT_URL, json=data, timeout=10)

#print(new_fight_response.status_code)
#print(new_fight_response.text)


#GET_BY_NAME_URL = "http://127.0.0.1:8000/competitor/Nikos+Kyriakopoulos"
#get_by_name_response = requests.get(GET_BY_NAME_URL, timeout=10)

#print(get_by_name_response.status_code)
#print(get_by_name_response.text)
