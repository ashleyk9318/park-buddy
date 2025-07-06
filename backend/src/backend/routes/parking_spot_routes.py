from flask import Blueprint, jsonify
from backend.api.parking_spots import get_parking_spots, get_parking_spot_by_id, get_parking_spot_by_spot_number, get_parking_spots_by_status
from backend.database.schema import SpotStatus

parking_spot_bp = Blueprint('parking_spot', __name__, url_prefix='/api')

@parking_spot_bp.route('/floors/<floor_id>/parking-spots/', methods=['GET'])
def api_get_parking_spots(floor_id):
    """Get all parking spots for a floor"""
    try:
        parking_spots = get_parking_spots(floor_id)
        return jsonify([{
            'spot_id': spot.spot_id,
            'floor_id': spot.floor_id,
            'spot_number': spot.spot_number,
            'status': spot.status.value,
            'last_update_timestamp': str(spot.last_update_timestamp)
        } for spot in parking_spots]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@parking_spot_bp.route('/parking-spots/<spot_id>/', methods=['GET'])
def api_get_parking_spot_by_id(spot_id):
    """Get parking spot by ID"""
    try:
        spot = get_parking_spot_by_id(spot_id)
        return jsonify({
            'spot_id': spot.spot_id,
            'floor_id': spot.floor_id,
            'spot_number': spot.spot_number,
            'status': spot.status.value,
            'last_update_timestamp': str(spot.last_update_timestamp)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@parking_spot_bp.route('/floors/<floor_id>/parking-spots/<spot_number>/', methods=['GET'])
def api_get_parking_spot_by_number(floor_id, spot_number):
    """Get parking spot by spot number and floor ID"""
    try:
        spot = get_parking_spot_by_spot_number(spot_number, floor_id)
        return jsonify({
            'spot_id': spot.spot_id,
            'floor_id': spot.floor_id,
            'spot_number': spot.spot_number,
            'status': spot.status.value,
            'last_update_timestamp': str(spot.last_update_timestamp)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@parking_spot_bp.route('/floors/<floor_id>/parking-spots/status/<status>/', methods=['GET'])
def api_get_parking_spots_by_status(floor_id, status):
    """Get parking spots by status for a floor"""
    try:
        # Convert string status to SpotStatus enum
        try:
            spot_status = SpotStatus(status.lower())
        except ValueError:
            return jsonify({'error': f'Invalid status: {status}. Valid statuses are: {[s.value for s in SpotStatus]}'}), 400
        
        parking_spots = get_parking_spots_by_status(floor_id, spot_status)
        return jsonify([{
            'spot_id': spot.spot_id,
            'floor_id': spot.floor_id,
            'spot_number': spot.spot_number,
            'status': spot.status.value,
            'last_update_timestamp': str(spot.last_update_timestamp)
        } for spot in parking_spots]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500 