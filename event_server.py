from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
events = []
attendees = {}
speakers_performers = {}  
vendors = {}
feedbacks = {}
budgets = {}

@app.route("/", methods=["GET"])
def list_events():
    """Returns the list of registered events along with attendees, speakers/performers, vendors, feedback, and budget."""
    event_data = []
    for event in events:
        event_id = event["id"]
        event_info = {
            "id": event_id,
            "name": event["name"],
            "date": event["date"],
            "attendees": attendees.get(event_id, []),
            "speakers_performers": speakers_performers.get(event_id, []),
            "feedback": feedbacks.get(event_id, []),
            "budget": budgets.get(event_id, "Not defined")
        }
        event_data.append(event_info)

    return jsonify({"events": event_data, "vendors": vendors})

@app.route("/create_event", methods=["POST"])
def create_event():
    """Creates a new event"""
    name = request.form.get("name")
    date = request.form.get("date")

    if not name or not date:
        return jsonify({"error": "Name and date are required"}), 400

    event_id = len(events) + 1
    event = {"id": event_id, "name": name, "date": date}
    events.append(event)

    return jsonify({"message": "Event successfully created", "event": event})

@app.route("/edit_event", methods=["PUT"])
def edit_event():
    """Edits an existing event"""
    event_id = request.form.get("event_id")
    name = request.form.get("name")
    date = request.form.get("date")

    if not event_id or not name or not date:
        return jsonify({"error": "ID, name, and date are required"}), 400

    event_id = int(event_id)
    if event_id > len(events) or event_id <= 0:
        return jsonify({"error": "Event not found"}), 404

    event = events[event_id - 1]
    event["name"] = name
    event["date"] = date

    return jsonify({"message": "Event successfully updated", "event": event})

@app.route("/register", methods=["POST"])
def register_attendee():
    """Registers an attendee for an event"""
    name = request.form.get("name")
    event_id = request.form.get("event_id")

    if not name or not event_id:
        return jsonify({"error": "Name and event ID are required"}), 400

    event_id = int(event_id)
    if event_id > len(events) or event_id <= 0:
        return jsonify({"error": "Event not found"}), 404

    if event_id not in attendees:
        attendees[event_id] = []

    attendees[event_id].append(name)

    return jsonify({"message": "Attendee successfully registered", "attendees": attendees[event_id]})

@app.route("/attendees", methods=["GET"])
def list_attendees():
    """Returns the list of registered attendees for each event"""
    return jsonify(attendees)

@app.route("/register_speaker_performer", methods=["POST"])
def register_speaker_performer():
    """Registers a speaker or performer for an event with a description"""
    name = request.form.get("name")
    event_id = request.form.get("event_id")
    description = request.form.get("description", "")

    if not name or not event_id:
        return jsonify({"error": "Name, event ID, and description are required"}), 400

    try:
        event_id = int(event_id)
    except ValueError:
        return jsonify({"error": "Event ID must be a number"}), 400

    if event_id > len(events) or event_id <= 0:
        return jsonify({"error": "Event not found"}), 404

    if event_id not in speakers_performers:
        speakers_performers[event_id] = []

    speakers_performers[event_id].append({"name": name, "description": description})

    return jsonify({
        "message": "Speaker/Performer successfully registered",
        "speakers_performers": speakers_performers[event_id]
    })

@app.route("/list_speakers_performers", methods=["GET"])
def list_speakers_performers():
    """Returns the list of registered speakers and performers for each event"""
    return jsonify(speakers_performers)

@app.route("/register_vendor", methods=["POST"])
def register_vendor():
    """Registers a vendor and their products/services"""
    name = request.form.get("name")
    products = request.form.get("products")

    if not name or not products:
        return jsonify({"error": "Vendor name and products/services are required"}), 400

    if name in vendors:
        return jsonify({"error": "Vendor already registered"}), 400

    vendors[name] = products.split(", ")

    return jsonify({"message": "Vendor successfully registered", "vendors": vendors})

@app.route("/list_vendors", methods=["GET"])
def list_vendors():
    """Returns the list of registered vendors"""
    return jsonify(vendors)

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    """Submits feedback for an event"""
    event_id = request.form.get("event_id")
    feedback = request.form.get("feedback")

    if not event_id or not feedback:
        return jsonify({"error": "Event ID and feedback are required"}), 400

    event_id = int(event_id)
    if event_id > len(events) or event_id <= 0:
        return jsonify({"error": "Event not found"}), 404

    if event_id not in feedbacks:
        feedbacks[event_id] = []

    feedbacks[event_id].append(feedback)
    return jsonify({"message": "Feedback successfully recorded", "feedbacks": feedbacks[event_id]})

@app.route("/get_feedback", methods=["GET"])
def get_feedback():
    """Retrieves feedback for an event"""
    event_id = request.args.get("event_id")

    if not event_id:
        return jsonify({"error": "Event ID is required"}), 400

    event_id = int(event_id)
    if event_id not in feedbacks:
        return jsonify([])

    return jsonify(feedbacks[event_id])

@app.route("/update_budget", methods=["POST"])
def update_budget():
    """Updates the budget for an event"""
    event_id = request.form.get("event_id")
    amount = request.form.get("amount")

    if not event_id or not amount:
        return jsonify({"error": "Event ID and budget amount are required"}), 400

    event_id = int(event_id)
    if event_id > len(events) or event_id <= 0:
        return jsonify({"error": "Event not found"}), 404

    budgets[event_id] = amount
    return jsonify({"message": "Budget successfully updated", "budget": budgets[event_id]})

@app.route("/get_budget", methods=["GET"])
def get_budget():
    """Retrieves the budget for an event"""
    event_id = request.args.get("event_id")

    if not event_id:
        return jsonify({"error": "Event ID is required"}), 400

    event_id = int(event_id)
    if event_id not in budgets:
        return jsonify({"error": "Budget not found"}), 404

    return jsonify({"budget": budgets[event_id]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
