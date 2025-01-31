import requests

BASE_URL = "http://127.0.0.1:5000"

def create_event(name, date):
    """Creates a new event"""
    response = requests.post(f"{BASE_URL}/create_event", data={"name": name, "date": date})
    return response.json()

def edit_event(event_id, name, date):
    """Edits an existing event"""
    response = requests.put(f"{BASE_URL}/edit_event", data={"event_id": event_id, "name": name, "date": date})
    return response.json()

def get_events():
    """Lists all registered events"""
    response = requests.get(f"{BASE_URL}/")
    return response.json()

def register_attendee(name, event_id):
    """Registers an attendee for an event"""
    response = requests.post(f"{BASE_URL}/register", data={"name": name, "event_id": event_id})
    return response.json()

def get_attendees():
    """Lists all registered attendees"""
    response = requests.get(f"{BASE_URL}/attendees")
    return response.json()

def register_speaker_or_performer(speaker_name, event_id, description):
    """Registers a speaker or performer for an event"""
    response = requests.post(
        f"{BASE_URL}/register_speaker_performer",
        data={"name": speaker_name, "event_id": event_id, "description": description}
    )
    return response.json()

def get_speakers_or_performers():
    """Lists all registered speakers and performers"""
    response = requests.get(f"{BASE_URL}/list_speakers_performers")
    return response.json()

def register_vendor(name, products):
    """Registers a vendor and their products/services"""
    response = requests.post(f"{BASE_URL}/register_vendor", data={"name": name, "products": products})
    return response.json()

def get_vendors():
    """Lists all registered vendors"""
    response = requests.get(f"{BASE_URL}/list_vendors")
    return response.json()

def submit_feedback(event_id, feedback):
    """Submits feedback for an event"""
    response = requests.post(f"{BASE_URL}/submit_feedback", data={"event_id": event_id, "feedback": feedback})
    return response.json()

def get_feedback(event_id):
    """Retrieves feedback for an event"""
    response = requests.get(f"{BASE_URL}/get_feedback", params={"event_id": event_id})
    return response.json()

def update_budget(event_id, amount):
    """Updates the budget for an event"""
    response = requests.post(f"{BASE_URL}/update_budget", data={"event_id": event_id, "amount": amount})
    return response.json()

def get_budget(event_id):
    """Retrieves the budget for an event"""
    response = requests.get(f"{BASE_URL}/get_budget", params={"event_id": event_id})
    return response.json()
