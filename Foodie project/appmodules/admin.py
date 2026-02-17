from flask import Blueprint, jsonify
import storage

admin_bp = Blueprint("admin_bp", __name__)

@admin_bp.route("/api/v1/admin/restaurants/<int:rid>/approve", methods=["PUT"])
def approve_restaurant(rid):
    if rid not in storage.restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    storage.restaurants[rid]["approved"] = True
    return jsonify({"message": "Restaurant approved"}), 200


@admin_bp.route("/api/v1/admin/restaurants/<int:rid>/disable", methods=["PUT"])
def admin_disable_restaurant(rid):
    if rid not in storage.restaurants:
        return jsonify({"error": "Restaurant Not Found"}), 404

    storage.restaurants[rid]["active"] = False
    return jsonify({"message": "Restaurant disabled by admin"}), 200


@admin_bp.route("/api/v1/admin/feedback", methods=["GET"])
def view_feedback():
    return jsonify(list(storage.ratings.values())), 200


@admin_bp.route("/api/v1/admin/orders", methods=["GET"])
def view_orders():
    return jsonify(list(storage.orders.values())), 200