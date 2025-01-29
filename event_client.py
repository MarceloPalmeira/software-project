import requests

BASE_URL = "http://127.0.0.1:5000"

def create_event(name, date):
    #cria um novo evento
    response = requests.post(f"{BASE_URL}/create_event", data={"name": name, "date": date})
    return response.json()

def get_events():
    #lista eventos cadastrados
    response = requests.get(f"{BASE_URL}/")
    return response.json()

def register_attendee(name, event_id):
    #registra um participante em um evento
    response = requests.post(f"{BASE_URL}/register", data={"name": name, "event_id": event_id})
    return response.json()

def get_attendees():
    #lista participantes registrados
    response = requests.get(f"{BASE_URL}/attendees")
    return response.json()
