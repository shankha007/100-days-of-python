import env
import requests
from datetime import datetime

HOST_DOMAIN = "https://trackapi.nutritionix.com"
NLP_ENDPOINT = "/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/bf734ee783145eaf1f35bcf17086a904/myWorkouts/workouts"

now = datetime.now()
current_date = now.strftime("%Y/%m/%d")
current_time = now.strftime("%H:%M:%S")

user_input = input("Tell me what exercises you did: ")

params = {
    "query": user_input
}

headers = {
    "x-app-id": env.APP_ID,
    "x-app-key": env.API_KEY,
    'Content-Type': "application/json",
}

response = requests.post(url=f"{HOST_DOMAIN}{NLP_ENDPOINT}", headers=headers, json=params)
data = response.json()['exercises']
exercises = [{"date": current_date, "time": current_time, "exercise": str(exercise["name"]).title(),
              "duration": str(exercise["duration_min"]), "calories": str(exercise["nf_calories"])} for exercise in
             data]

sheety_header = {
    'Content-Type': "application/json",
    'Authorization': f"Bearer {env.SHEETY_BEARER_TOKEN}"
}

for exercise in exercises:
    json_body = {"workout": exercise}
    res = requests.post(url=SHEETY_ENDPOINT, headers=sheety_header, json=json_body)
    print(res.text)
