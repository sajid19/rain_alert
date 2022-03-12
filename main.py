import requests
from twilio.rest import Client

End_point = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "68779693b03322b5e577c561a075c7ae"
account_sid = "ACa5a2a407a7317d404671d5c0295ac61a"
auth_token = "79e5955c206ee6eaf18073ea7d4f2b08"

weather_parameter = {
    "lat": 28.454863,
    "lon": 117.943436,
    "appid": api_key,
    "exclude":"current,minutely,daily"

}

response = requests.get(End_point, params=weather_parameter)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    weather_code = hour_data["weather"][0]["id"]
    if int(weather_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to be rain today.Bring Umbrella ☂ ",
        from_='+19362377630',
        to ='+8801780434555'
   )
    print(message.status)

















