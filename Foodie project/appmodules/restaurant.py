from flask import Blueprint, request, jsonify
import storage

restaurant_bp = Blueprint("restaurant_bp", __name__)

@restaurant_bp.route("/api/v1/restaurants", methods=["POST"])
def register_restaurant():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Restaurant name required"}), 400

    rid = storage.restaurant_id_counter

    restaurant = {
        "id": rid,
        "name": data.get("name"),
        "category": data.get("category", ""),
        "location": data.get("location", ""),
        "contact": data.get("contact", ""),
        "approved": False,
        "active": True
    }

    storage.restaurants[rid] = restaurant
    storage.restaurant_id_counter += 1

    return jsonify(restaurant), 201


@restaurant_bp.route("/api/v1/restaurants/<int:rid>", methods=["PUT"])
def update_restaurant(rid):
    if rid not in storage.restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    data = request.json
    storage.restaurants[rid]["name"] = data.get("name", storage.restaurants[rid]["name"])
    storage.restaurants[rid]["location"] = data.get("location", storage.restaurants[rid]["location"])

    return jsonify(storage.restaurants[rid]), 200


@restaurant_bp.route("/api/v1/restaurants/<int:rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    if rid not in storage.restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    storage.restaurants[rid]["active"] = False
    return jsonify({"message": "Restaurant disabled"}), 200


@restaurant_bp.route("/api/v1/restaurants/<int:rid>", methods=["GET"])
def view_restaurant(rid):
    if rid not in storage.restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    return jsonify(storage.restaurants[rid]), 200


@restaurant_bp.route("/api/v1/restaurants", methods=["GET"])
def view_all_restaurants():
    return jsonify(list(storage.restaurants.values())), 200