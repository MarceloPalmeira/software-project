from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de dados em memória
events = []
attendees = {}

@app.route("/", methods=["GET"])
def list_events():
    """Retorna a lista de eventos cadastrados junto com os participantes"""
    event_data = []
    for event in events:
        event_id = event["id"]
        event_info = {
            "id": event_id,
            "name": event["name"],
            "date": event["date"],
            "attendees": attendees.get(event_id, [])  # Obtém participantes ou lista vazia
        }
        event_data.append(event_info)

    return jsonify(event_data)

@app.route("/create_event", methods=["POST"])
def create_event():
    """Cria um novo evento"""
    name = request.form.get("name")
    date = request.form.get("date")

    if not name or not date:
        return jsonify({"error": "Nome e data são obrigatórios"}), 400

    event_id = len(events) + 1
    event = {"id": event_id, "name": name, "date": date}
    events.append(event)

    return jsonify({"message": "Evento criado com sucesso", "event": event})

@app.route("/register", methods=["POST"])
def register_attendee():
    """Registra um participante em um evento"""
    name = request.form.get("name")
    event_id = request.form.get("event_id")

    if not name or not event_id:
        return jsonify({"error": "Nome e ID do evento são obrigatórios"}), 400

    event_id = int(event_id)
    if event_id > len(events) or event_id <= 0:
        return jsonify({"error": "Evento não encontrado"}), 404

    if event_id not in attendees:
        attendees[event_id] = []

    attendees[event_id].append(name)

    return jsonify({"message": "Participante registrado com sucesso", "attendees": attendees[event_id]})

@app.route("/attendees", methods=["GET"])
def list_attendees():
    """Retorna a lista de participantes registrados em cada evento"""
    return jsonify(attendees)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
