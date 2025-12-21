from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from models import User

def admin_required(fn):
    """
    Decorator to require admin role for accessing certain routes
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            current_user_id = get_jwt_identity()
            user = User.query.get(current_user_id)
            
            if not user or not user.is_admin():
                return jsonify({'message': 'Admin access required'}), 403
                
            if user.is_blocked:
                return jsonify({'message': 'User is blocked'}), 403
                
            return fn(*args, **kwargs)
        except Exception as e:
            return jsonify({'message': 'Authentication failed'}), 401
    return wrapper

def user_required(fn):
    """
    Decorator to require authenticated user for accessing certain routes
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            current_user_id = get_jwt_identity()
            user = User.query.get(current_user_id)
            
            if not user:
                return jsonify({'message': 'User not found'}), 404
                
            if user.is_blocked:
                return jsonify({'message': 'User is blocked'}), 403
                
            return fn(*args, **kwargs)
        except Exception as e:
            return jsonify({'message': 'Authentication failed'}), 401
    return wrapper

def get_current_user():
    """
    Get the current authenticated user
    """
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        return user
    except:
        return None