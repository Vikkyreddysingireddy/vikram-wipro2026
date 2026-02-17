from flask import Blueprint, request, jsonify
import storage

order_bp = Blueprint("order_bp", __name__)

@order_bp.route("/api/v1/orders", methods=["POST"])
def place_order():
    data = request.json
    if not data or "user_id" not in data or "restaurant_id" not in data:
        return jsonify({"error": "Missing order details"}), 400

    oid = storage.order_id_counter

    order = {
        "id": oid,
        "user_id": data["user_id"],
        "restaurant_id": data["restaurant_id"],
        "dish": data.get("dish"),
        "status": "Pending"
    }

    storage.orders[oid] = order
    storage.order_id_counter += 1

    return jsonify(order), 201


@order_bp.route("/api/v1/ratings", methods=["POST"])
def give_rating():
    data = request.json

    rid = storage.rating_id_counter

    rating = {
        "id": rid,
        "order_id": data["order_id"],
        "rating": data["rating"],
        "comment": data.get("comment")
    }

    storage.ratings[rid] = rating
    storage.rating_id_counter += 1

    return jsonify(rating), 201


@order_bp.route("/api/v1/restaurants/<int:rid>/orders", methods=["GET"])
def orders_by_restaurant(rid):
    result = [o for o in storage.orders.values() if o["restaurant_id"] == rid]
    return jsonify(result), 200


@order_bp.route("/api/v1/users/<int:uid>/orders", methods=["GET"])
def orders_by_user(uid):
    result = [o for o in storage.orders.values() if o["user_id"] == uid]
    return jsonify(result), 200