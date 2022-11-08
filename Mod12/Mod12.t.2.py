import requests as requests

api_key = "c4d5e93c09467c67be48ac4cea78e738"
city = input("Enter city name : ")
complete_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response = requests.get(complete_url)

answ = response.json()

if answ["cod"] != "404":

    y = answ["main"]

    current_temperature = y["temp"]
    z = answ["weather"]
    weather_description = z[0]["description"]
    print(" Temperature is " + str(current_temperature) + " degrees Celsius and  " + str(
        weather_description))

else:
    print(" City Not Found ")
