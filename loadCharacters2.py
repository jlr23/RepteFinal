import requests
import json
import random

cities = [
    {"name": "Tokyo", "latitude": 35.682839, "longitude": 139.759455},
    {"name": "Delhi", "latitude": 28.644800, "longitude": 77.216721},
    {"name": "Shanghai", "latitude": 31.230391, "longitude": 121.473701},
    {"name": "Sao Paulo", "latitude": -23.550520, "longitude": -46.633308},
    {"name": "Mexico City", "latitude": 19.432608, "longitude": -99.133209},
    {"name": "Cairo", "latitude": 30.044420, "longitude": 31.235712},
    {"name": "Dhaka", "latitude": 23.810331, "longitude": 90.412521},
    {"name": "Mumbai", "latitude": 19.076090, "longitude": 72.877426},
    {"name": "Beijing", "latitude": 39.904202, "longitude": 116.407394},
    {"name": "Osaka", "latitude": 34.693738, "longitude": 135.502165},
    {"name": "Karachi", "latitude": 24.860735, "longitude": 67.001137},
    {"name": "Chongqing", "latitude": 29.563760, "longitude": 106.550464},
    {"name": "Istanbul", "latitude": 41.008238, "longitude": 28.978359},
    {"name": "Buenos Aires", "latitude": -34.603684, "longitude": -58.381559},
    {"name": "Kolkata", "latitude": 22.572646, "longitude": 88.363895},
    {"name": "Kinshasa", "latitude": -4.441931, "longitude": 15.266293},
    {"name": "Lagos", "latitude": 6.524379, "longitude": 3.379206},
    {"name": "Manila", "latitude": 14.599512, "longitude": 120.984222},
    {"name": "Rio de Janeiro", "latitude": -22.906847, "longitude": -43.172896},
    {"name": "Guangzhou", "latitude": 23.129110, "longitude": 113.264385},
    {"name": "Los Angeles", "latitude": 34.052235, "longitude": -118.243683},
    {"name": "Moscow", "latitude": 55.755825, "longitude": 37.617298},
    {"name": "Shenzhen", "latitude": 22.542883, "longitude": 114.059567},
    {"name": "Lahore", "latitude": 31.549719, "longitude": 74.343618},
    {"name": "Bangalore", "latitude": 12.971599, "longitude": 77.594566},
    {"name": "Paris", "latitude": 48.856613, "longitude": 2.352222},
    {"name": "Bogota", "latitude": 4.711000, "longitude": -74.072090},
    {"name": "Jakarta", "latitude": -6.208763, "longitude": 106.845599},
    {"name": "Chennai", "latitude": 13.082680, "longitude": 80.270718},
    {"name": "Lima", "latitude": -12.046374, "longitude": -77.042793},
    {"name": "Bangkok", "latitude": 13.756331, "longitude": 100.501765},
    {"name": "Seoul", "latitude": 37.566536, "longitude": 126.977966},
    {"name": "Nagoya", "latitude": 35.181446, "longitude": 136.906398},
    {"name": "Hyderabad", "latitude": 17.385044, "longitude": 78.486671},
    {"name": "London", "latitude": 51.507351, "longitude": -0.127758},
    {"name": "Tehran", "latitude": 35.689198, "longitude": 51.388974},
    {"name": "Chicago", "latitude": 41.878113, "longitude": -87.629799},
    {"name": "Chengdu", "latitude": 30.572269, "longitude": 104.066541},
    {"name": "Nanjing", "latitude": 32.060255, "longitude": 118.796877},
    {"name": "Wuhan", "latitude": 30.592850, "longitude": 114.305539},
    {"name": "Ho Chi Minh City", "latitude": 10.823099, "longitude": 106.629664},
    {"name": "Luanda", "latitude": -8.839988, "longitude": 13.289437},
    {"name": "Ahmedabad", "latitude": 23.022505, "longitude": 72.571362},
    {"name": "Kuala Lumpur", "latitude": 3.139003, "longitude": 101.686855},
    {"name": "Xi'an", "latitude": 34.341568, "longitude": 108.939770},
    {"name": "Hong Kong", "latitude": 22.396428, "longitude": 114.109497},
    {"name": "Dongguan", "latitude": 23.020536, "longitude": 113.751765},
    {"name": "Hangzhou", "latitude": 30.274085, "longitude": 120.155070},
    {"name": "Foshan", "latitude": 23.021478, "longitude": 113.121435},
    {"name": "Shenyang", "latitude": 41.805699, "longitude": 123.431472},
    {"name": "Riyadh", "latitude": 24.713552, "longitude": 46.675296},
    {"name": "Baghdad", "latitude": 33.315241, "longitude": 44.366066},
    {"name": "Santiago", "latitude": -33.448890, "longitude": -70.669265},
    {"name": "Surat", "latitude": 21.170240, "longitude": 72.831062},
    {"name": "Madrid", "latitude": 40.416775, "longitude": -3.703790},
    {"name": "Suzhou", "latitude": 31.298979, "longitude": 120.585290},
    {"name": "Pune", "latitude": 18.520430, "longitude": 73.856744},
    {"name": "Harbin", "latitude": 45.803775, "longitude": 126.534967},
    {"name": "Houston", "latitude": 29.760427, "longitude": -95.369804},
    {"name": "Dallas", "latitude": 32.776665, "longitude": -96.796989},
    {"name": "Toronto", "latitude": 43.653226, "longitude": -79.383184},
    {"name": "Dar es Salaam", "latitude": -6.792354, "longitude": 39.208328},
    {"name": "Miami", "latitude": 25.761680, "longitude": -80.191790},
    {"name": "Belo Horizonte", "latitude": -19.916681, "longitude": -43.934493},
    {"name": "Singapore", "latitude": 1.352083, "longitude": 103.819836},
    {"name": "Philadelphia", "latitude": 39.952584, "longitude": -75.165222},
    {"name": "Atlanta", "latitude": 33.749001, "longitude": -84.387978},
    {"name": "Fukuoka", "latitude": 33.590355, "longitude": 130.401716},
    {"name": "Khartoum", "latitude": 15.500654, "longitude": 32.559899},
    {"name": "Barcelona", "latitude": 41.385064, "longitude": 2.173404},
    {"name": "Johannesburg", "latitude": -26.204103, "longitude": 28.047305},
]




def obtenir_informacio(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()   
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")
        return None

def realizar_post(data):
    url ='https://retoolapi.dev/O4IXtN/characters2'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response

def numero_aleatorioK():
    return random.randint(1000, 2000)

def numero_aleatorio():
    return random.randint(2, 70)

def main():
    lista_json = []
    url = 'https://dragonball-api.com/api/characters?&limit=5'
    personajes_lista = []
    data = obtenir_informacio(url)
    meta_info = data.get('meta', {})
    links_info = data.get('links',{})
    url = links_info['next']
    last_page = meta_info['totalPages']
    if data and 'items' in data:
        personajes_lista = data['items']
    
    for i in range(1, last_page + 1):
        if not url:
            break
        data = obtenir_informacio(url)
        links_info = data.get('links',{})
        url = links_info['next']
        if data and 'items' in data:
            personajes_lista.extend(data['items'])
        
    i=0
    for personaje in personajes_lista:
        data = {
            "id": i+3,
            "Name": personaje['name'],
            "Life": numero_aleatorioK(),
            "Dodge": numero_aleatorio(),
            "IdUser": 1
        }
        lista_json.append(data)        
        i+=1
        response = realizar_post(data)
        print(response.status_code)
        print(response.json())



if __name__ == "__main__":
    main()