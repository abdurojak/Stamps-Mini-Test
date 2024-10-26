import requests
from datetime import datetime, timedelta

API_KEY = '4ad9126a1f97c33e5930db5297993398'
CITY = "jakarta"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code == 200 and data.get("list"):
    print(f"Prakiraan Cuaca 5 Hari untuk {CITY}:\n")
    
    last_date = None
    for forecast in data["list"]:
        date_text = forecast["dt_txt"]
        date_obj = datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S")
        
        if last_date != date_obj.date():
            formatted_date = date_obj.strftime('%a, %d %b %Y')
            temp = forecast["main"]["temp"]
            print(f"{formatted_date}: {temp:.2f}°C")
            last_date = date_obj.date()
else:
    print("Gagal mengambil data. Periksa API key atau nama kota.")