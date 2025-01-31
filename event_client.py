import requests

BASE_URL = "http://127.0.0.1:5000"

def create_event(name, date):
    #cria um novo evento
    response = requests.post(f"{BASE_URL}/create_event", data={"name": name, "date": date})
    return response.json()

def edit_event(event_id, name, date):
    #edita um evento existente
    response = requests.put(f"{BASE_URL}/edit_event", data={"event_id": event_id, "name": name, "date": date})
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

def register_speaker_or_performer(speaker_name, event_id, description):
    response = requests.post(
        f"{BASE_URL}/register_speaker_performer",
        data={"name": speaker_name, "event_id": event_id, "description": description}
    )
    return response.json()

def edit_speaker_or_performer(event_id, old_name, new_name=None, new_description=None):
    data = {"event_id": event_id, "old_name": old_name}
    if new_name:
        data["new_name"] = new_name
    if new_description:
        data["new_description"] = new_description

    response = requests.put(f"{BASE_URL}/edit_speaker_performer", data=data)
    return response.json()

def get_speakers_or_performers():
    response = requests.get(f"{BASE_URL}/list_speakers_performers")
    return response.json()

