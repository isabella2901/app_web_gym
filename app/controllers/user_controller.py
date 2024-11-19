from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from app.services.user_service import UserService


user_bp = Blueprint("user_bp", __name__)
user_service = UserService()


@cross_origin()
@user_bp.route("/users", methods=["GET"])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users), 200


@cross_origin()
@user_bp.route("/users/<string:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 500


@cross_origin()
@user_bp.route("/users", methods=["POST"])
def create_user():
    user_data = request.json
    new_user = user_service.create_user(user_data)
    return jsonify(new_user), 201


@cross_origin()
@user_bp.route("/users/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    updated_data = request.json
    updated_user = user_service.update_user(user_id, updated_data)
    if updated_user:
        return jsonify(updated_user), 200
    return jsonify({"message": "User not found"}), 500


@cross_origin()
@user_bp.route("/users/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user_service.delete_user(user_id)
    return jsonify({"message": "User deleted"}), 500
