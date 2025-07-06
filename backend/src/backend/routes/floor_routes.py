from flask import Blueprint, jsonify
from backend.api.floor import get_floors, get_floor_by_id, get_floor_by_floor_number

floor_bp = Blueprint('floor', __name__, url_prefix='/api')

@floor_bp.route('/garages/<garage_id>/floors/', methods=['GET'])
def api_get_floors(garage_id):
    """Get all floors for a garage"""
    try:
        floors = get_floors(garage_id)
        return jsonify([{
            'floor_id': floor.floor_id,
            'garage_id': floor.garage_id,
            'floor_number': floor.floor_number,
            'last_update_timestamp': str(floor.last_update_timestamp)
        } for floor in floors]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@floor_bp.route('/floors/<floor_id>/', methods=['GET'])
def api_get_floor_by_id(floor_id):
    """Get floor by ID"""
    try:
        floor = get_floor_by_id(floor_id)
        return jsonify({
            'floor_id': floor.floor_id,
            'garage_id': floor.garage_id,
            'floor_number': floor.floor_number,
            'last_update_timestamp': str(floor.last_update_timestamp)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@floor_bp.route('/garages/<garage_id>/floors/<floor_number>/', methods=['GET'])
def api_get_floor_by_number(garage_id, floor_number):
    """Get floor by floor number and garage ID"""
    try:
        floor = get_floor_by_floor_number(floor_number, garage_id)
        return jsonify({
            'floor_id': floor.floor_id,
            'garage_id': floor.garage_id,
            'floor_number': floor.floor_number,
            'last_update_timestamp': str(floor.last_update_timestamp)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500 