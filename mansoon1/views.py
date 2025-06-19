from django.shortcuts import render
import requests

def home(request):
    query = ""
    context = {}
    if request.method == "POST":
        query = request.POST["q"]
        city = query.upper()
        key = "7a8457caf38e3cc928ffb1efd7953401"
        api = f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={key}"

        response = requests.get(api)
        if response.status_code == 200:
            data = response.json()
            context = {
                'city': city,
                "temp": int(data["main"]["temp"] - 273.15),
                "wind": data["wind"]["speed"],
                "humidity": data["main"]["humidity"],
                "sys": data["sys"]["country"],
                "desc": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"]
            }
        else:
            error = "City Not Found"
            context = {
                "error":error
            }
    return render(request, 'index.html', context)