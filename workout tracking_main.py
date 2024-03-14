import requests
import datetime as dt

APP_ID = "ENTER TOKEN"
API_KEY = "ENTER TOKEN"
END_POINT = "v2/natural/exercise"
WEIGHT = 52
HEIGHT = 172
AGE = 23

parameters = {
    "query": input("What exercise you have done today?:\n"),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(
    url=f"https://trackapi.nutritionix.com/{END_POINT}", 
    json=parameters,
    headers=headers)
data = response.json()
print(data)

time = dt.datetime
now = time.now()
date = now.strftime(r"%d/%m/%Y")
timing = now.strftime(r"%X")

bearer_headers = {
    "Authorization":"Bearer ENTER TOKEN"

}

for exercise in data["exercises"]:
    sheet_data = {
        "workout":{
        "date": date,
        "time": timing,
        "exercise": exercise["user_input"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
        }
    }
    #print(sheet_data)


    sheet = requests.post(
    url="https://api.sheety.co/.../workout/workouts",
    json=sheet_data,
    headers=bearer_headers)
    #print(sheet.text)
#print(sheet_data)