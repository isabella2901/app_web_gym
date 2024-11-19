from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from app.services.exercices_services import ExercicesService


exercise_bp = Blueprint("exercise_bp", __name__)
exercises_service = ExercicesService()


@cross_origin()
@exercise_bp.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = exercises_service.get_all_exercises()
    return jsonify(exercises), 200
