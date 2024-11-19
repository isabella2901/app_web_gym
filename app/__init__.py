from flask import Flask, jsonify, request
from app.controllers import user_controller, exercices_controller  # Importa el controlador

from flask_cors import CORS,cross_origin


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Registrar el blueprint del controlador
    app.register_blueprint(user_controller.user_bp)
    app.register_blueprint(exercices_controller.exercise_bp)

    return app
