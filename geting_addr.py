import requests
import json
from celery import Celery

#celery init
app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task(bind=True)
def get_nearest_rest(self, address, api_key):
    if not address:
        return -2
    try:
        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&format=json&geocode={address}"
        responce=requests.get(geocoder_request)
        if responce.status_code == 200:
            json_responce = responce.json()
            coordinates=json_responce["responce"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['Point']['pos'].split()
            lon, lat = coordinates[0], coordinates[1]
        else:
            return 0 #eror while geocoding
        
    except Exception as e:
        return str(e)
        
    try:
        search_request = f"https://search-maps.yandex.ru/v1/?apikey={api_key}&text=буше&ll={lon},{lat}&langru_RU&resylts=1"
        responce = requests.get(search_request)
        if responce.status_code == 200:
            json_responce = responce.json()
            bushe_address = json_responce["features"][0]["properties"]["name"]
            return bushe_address
        else:
            return responce.status_code #error while finding //TODO: replace with num in PROD!!!
    except Exception as e:
        return str(e)