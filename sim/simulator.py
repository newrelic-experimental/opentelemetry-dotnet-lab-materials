import random
import requests
import time

while(True):
    requests.get("https://localhost:7072/WeatherForecast", verify=False)
    time.sleep(random.randint(5, 15))
