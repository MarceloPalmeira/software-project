from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de dados em memória
events = []
attendees = {}
speakers_performers = {}  


@app.route("/", methods=["GET"])
def list_events():
    """Retorna a lista de eventos cadastrados junto com os participantes e palestrantes/artistas"""
    event_data = []
    for event in events:
        event_id = event["id"]
        event_info = {
            "id": event_id,
            "name": event["name"],
            "date": event["date"],
            "attendees": attendees.get(event_id, []),  # Obtém participantes ou lista vazia
            "speakers_performers": speakers_performers.get(event_id, [])  # Obtém palestrantes/artistas ou lista vazia
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

@app.route("/edit_event", methods=["PUT"])
def edit_event():
    """Edita um evento existente"""
    event_id = request.form.get("event_id")
    name = request.form.get("name")
    date = request.form.get("date")

    if not event_id or not name or not date:
        return jsonify({"error": "ID, nome e data são obrigatórios"}), 400

    event_id = int(event_id)
    if event_id > len(events) or event_id <= 0:
        return jsonify({"error": "Evento não encontrado"}), 404

    event = events[event_id - 1]
    event["name"] = name
    event["date"] = date

    return jsonify({"message": "Evento editado com sucesso", "event": event})


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

# Adicionar estrutura para armazenar palestrantes e artistas
speakers_performers = {}

@app.route('/register_speaker_performer', methods=['POST'])
def register_speaker_performer():
    """Registra um palestrante ou artista em um evento com descrição"""
    name = request.form.get('name')
    event_id = request.form.get('event_id')
    description = request.form.get('description', '')  # Permite descrição vazia

    if not name or not event_id:
        return jsonify({"error": "Nome, ID do evento e descrição são obrigatórios"}), 400

    try:
        event_id = int(event_id)
    except ValueError:
        return jsonify({"error": "ID do evento deve ser um número"}), 400

    if event_id > len(events) or event_id <= 0:
        return jsonify({"error": "Evento não encontrado"}), 404

    if event_id not in speakers_performers:
        speakers_performers[event_id] = []

    # Adiciona o palestrante/artista na lista com a descrição
    speakers_performers[event_id].append({"name": name, "description": description})

    return jsonify({
        "message": "Palestrante/Artista registrado com sucesso",
        "speakers_performers": speakers_performers[event_id]
    })

@app.route('/edit_speaker_performer', methods=['PUT'])
def edit_speaker_performer():
    """Edita o nome e/ou a descrição de um palestrante ou artista em um evento"""
    event_id = request.form.get('event_id')
    old_name = request.form.get('old_name')
    new_name = request.form.get('new_name', None)
    new_description = request.form.get('new_description', None)

    if not event_id or not old_name:
        return jsonify({"error": "ID do evento e nome do participante são obrigatórios"}), 400

    try:
        event_id = int(event_id)
    except ValueError:
        return jsonify({"error": "ID do evento deve ser um número"}), 400

    if event_id > len(events) or event_id <= 0:
        return jsonify({"error": "Evento não encontrado"}), 404

    if event_id not in speakers_performers:
        return jsonify({"error": "Evento não possui palestrantes ou artistas"}), 404

    for speaker in speakers_performers[event_id]:
        if speaker["name"] == old_name:
            if new_name:
                speaker["name"] = new_name
            if new_description:
                speaker["description"] = new_description
            return jsonify({
                "message": "Palestrante/Artista editado com sucesso",
                "speakers_performers": speakers_performers[event_id]
            })

    return jsonify({"error": "Palestrante/Artista não encontrado"}), 404

@app.route('/list_speakers_performers', methods=['GET'])
def list_speakers_performers():
    """Retorna a lista de palestrantes e artistas registrados em cada evento"""
    return jsonify(speakers_performers)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
