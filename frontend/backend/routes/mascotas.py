from flask import Blueprint, jsonify, request
from services.mascota_service import obtener_mascotas, agregar_mascota

mascotas_bp = Blueprint('mascotas', __name__)

@mascotas_bp.route('/api/mascotas', methods=['GET'])
def get_mascotas():
    mascotas = obtener_mascotas()
    return jsonify([m.to_dict() for m in mascotas])

@mascotas_bp.route('/api/mascotas', methods=['POST'])
def post_mascota():
    data = request.get_json()
    nombre = data.get("nombre")
    especie = data.get("especie")

    if not nombre or not especie:
        return jsonify({"error": "Faltan datos"}), 400

    nueva = agregar_mascota(nombre, especie)
    return jsonify(nueva.to_dict()), 201
