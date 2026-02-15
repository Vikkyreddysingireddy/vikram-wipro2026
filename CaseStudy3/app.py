from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

patients = []
pid = 1


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/patients", methods=["GET"])
def get_patients():
    return jsonify(patients)

@app.route("/api/patients", methods=["POST"])
def add_patient():
    global pid
    data = request.json

    if not data.get("name") or not data.get("age"):
        return jsonify({"error": "Invalid data"}), 400

    data["id"] = pid
    pid += 1
    patients.append(data)

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
