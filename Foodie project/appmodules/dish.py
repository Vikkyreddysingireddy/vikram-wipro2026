from flask import Blueprint, request, jsonify
import storage

dish_bp = Blueprint("dish_bp", __name__)
@dish_bp.route("/api/v1/restaurants/<int:rid>/dishes", methods=["POST"])
def add_dish(rid):

    if rid not in storage.restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body required"}), 400

    if "name" not in data or "price" not in data:
        return jsonify({"error": "Dish name and price required"}), 400

    did = storage.dish_id_counter

    dish = {
        "id": did,
        "restaurant_id": rid,
        "name": data["name"],
        "price": data["price"],
        "enabled": True
    }

    storage.dishes[did] = dish
    storage.dish_id_counter += 1

    return jsonify(dish), 201

@dish_bp.route("/api/v1/restaurants/<int:rid>/dishes/<int:did>", methods=["PUT"])
def update_dish(rid, did):
    if rid not in storage.restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    if did not in storage.dishes:
        return jsonify({"error": "Dish Not Found"}), 404

    if storage.dishes[did]["restaurant_id"] != rid:
        return jsonify({"error": "Dish does not belong to this restaurant"}), 400

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body required"}), 400

    if "name" in data:
        storage.dishes[did]["name"] = data["name"]

    if "price" in data:
        storage.dishes[did]["price"] = data["price"]

    return jsonify(storage.dishes[did]), 200

@dish_bp.route("/api/v1/restaurants/<int:rid>/dishes/<int:did>/status", methods=["PUT"])
def enable_disable_dish(rid, did):

    if rid not in storage.restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    if did not in storage.dishes:
        return jsonify({"error": "Dish Not Found"}), 404

    if storage.dishes[did]["restaurant_id"] != rid:
        return jsonify({"error": "Dish does not belong to this restaurant"}), 400

    data = request.get_json()

    if not data or "enabled" not in data:
        return jsonify({"error": "Enabled field required"}), 400

    storage.dishes[did]["enabled"] = data["enabled"]

    return jsonify({
        "message": "Dish status updated",
        "dish": storage.dishes[did]
    }), 200

@dish_bp.route("/api/v1/restaurants/<int:rid>/dishes/<int:did>", methods=["DELETE"])
def delete_dish(rid, did):

    if rid not in storage.restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    if did not in storage.dishes:
        return jsonify({"error": "Dish Not Found"}), 404

    if storage.dishes[did]["restaurant_id"] != rid:
        return jsonify({"error": "Dish does not belong to this restaurant"}), 400

    deleted_dish = storage.dishes.pop(did)

    return jsonify({
        "message": "Dish deleted successfully",
        "deleted": deleted_dish
    }), 200