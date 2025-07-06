from flask import Blueprint, jsonify
from backend.api.garage import get_garages, get_garage_by_id, get_garage_by_location

garage_bp = Blueprint('garage', __name__, url_prefix='/api/garages')

@garage_bp.route('/', methods=['GET'])
def api_get_garages():
    """Get all garages"""
    try:
        garages = get_garages()
        return jsonify([{
            'garage_id': garage.garage_id,
            'location': garage.location,
            'last_update_timestamp': str(garage.last_update_timestamp)
        } for garage in garages]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@garage_bp.route('/<garage_id>/', methods=['GET'])
def api_get_garage_by_id(garage_id):
    """Get garage by ID"""
    try:
        garage = get_garage_by_id(garage_id)
        return jsonify({
            'garage_id': garage.garage_id,
            'location': garage.location,
            'last_update_timestamp': str(garage.last_update_timestamp)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@garage_bp.route('/location/<location>/', methods=['GET'])
def api_get_garage_by_location(location):
    """Get garage by location"""
    try:
        garage = get_garage_by_location(location)
        return jsonify({
            'garage_id': garage.garage_id,
            'location': garage.location,
            'last_update_timestamp': str(garage.last_update_timestamp)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500 