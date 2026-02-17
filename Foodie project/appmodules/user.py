from flask import Blueprint, request, jsonify
import storage

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/api/v1/users/register", methods=["POST"])
def register_user():
    data = request.json
    if not data or "email" not in data:
        return jsonify({"error": "Email required"}), 400

    uid = storage.user_id_counter

    user = {
        "id": uid,
        "name": data.get("name"),
        "email": data.get("email"),
        "password": data.get("password")
    }

    storage.users[uid] = user
    storage.user_id_counter += 1

    return jsonify(user), 201


@user_bp.route("/api/v1/restaurants/search", methods=["GET"])
def search_restaurants():
    name = request.args.get("name", "")
    result = [r for r in storage.restaurants.values() if name.lower() in r["name"].lower()]
    return jsonify(result), 200