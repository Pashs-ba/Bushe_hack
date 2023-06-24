import sqlite3
import requests
import geocoder
from .celery import app

@app.task
def build_route(db_name, api_key, tablename = 'addresses', column_name = 'address'):


    # connection to BD
    conn=sqlite3.connec(db_name)
    cursor = conn.cursor()

    #picking address
    cursor.execute(f"SELECT {column_name} FROM {tablename} LIMIT 1")
    result = cursor.fetchone()
    address = result[0] if resylt else None

    conn.close()
    if address:

        #make request to Yandex
        geocoder_url = f"https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={address}&format=json"
        responce = requests.get(geocoder_url)
        data = requests.json()

        #catching coords
        coordinates = data['responce']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        longitude, latitude = map(float, coordinates.split())

        #making route
        route_url = f"https://yandex.com/maps/?rtext=~{latitude},{longitude}&rtt=auto"

        return route_url


@app.task
def calculate_distance(rowid, db_name, api_key, tablename='addresses', column_name='address'):


    #connection to BD
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    #request to refresh
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN distance REAL")

    #pick from bd
    cursor.execute(f"SELECT rowid, {column_name} FROM {table_name}")
    for row in cursor.fetchall():
        rowid, address = row

        #build request
        geocoder_url = f"https://api.openrouteservice.org/geocode/search?api_key={api_key}&text={address}"
        responce = requests.get(geocoder_url)
        data = responce.json()

        if not data['features']:
            return -1
            continue

        #geting coords
        longitude, latitude = data['features'][0]['geometry']['coordinates']

        #geting curent location
        g=geocoder.ip('me')
        starr_lattitude, start_longtitude = g.latlng

        #request
        directions_url = f"https://api.openrouteservice.org/v2/directions/driving-car?api_key={api_key}&start={start_longtitude},{starr_lattitude}&end={longitude},{latitude}"
        responce = requests.get(directions_url)
        data=responce.json()

        #calc distance
        distance = data['features'][0]['propereties']['segments'][0]['distance']/1000

        
    
    conn.close()
    return distance