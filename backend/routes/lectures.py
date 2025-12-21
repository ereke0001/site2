from flask import Blueprint, request, jsonify
from models import db, Lecture

lectures_bp = Blueprint('lectures', __name__)

@lectures_bp.route('/api/lectures', methods=['GET'])
def get_lectures():
    try:
        lectures = Lecture.query.all()
        return jsonify({
            'lectures': [lecture.to_dict() for lecture in lectures]
        }), 200
    except Exception as e:
        return jsonify({'message': 'Failed to retrieve lectures', 'error': str(e)}), 500

@lectures_bp.route('/api/lectures/<int:lecture_id>', methods=['GET'])
def get_lecture(lecture_id):
    try:
        lecture = Lecture.query.get(lecture_id)
        if not lecture:
            return jsonify({'message': 'Lecture not found'}), 404
        
        return jsonify({'lecture': lecture.to_dict()}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to retrieve lecture', 'error': str(e)}), 500

@lectures_bp.route('/api/lectures', methods=['POST'])
#@admin_required
def create_lecture():
    try:
        data = request.get_json()
        
        # Validate input
        if not data or not data.get('title') or not data.get('content'):
            return jsonify({'message': 'Title and content are required'}), 400
        
        # Create new lecture
        lecture = Lecture(
            title=data['title'],
            content=data['content']
        )
        
        db.session.add(lecture)
        db.session.commit()
        
        return jsonify({
            'message': 'Lecture created successfully',
            'lecture': lecture.to_dict()
        }), 201
    except Exception as e:
        return jsonify({'message': 'Failed to create lecture', 'error': str(e)}), 500

@lectures_bp.route('/api/lectures/<int:lecture_id>', methods=['PUT'])
def update_lecture(lecture_id):
    try:
        lecture = Lecture.query.get(lecture_id)
        if not lecture:
            return jsonify({'message': 'Lecture not found'}), 404
        
        data = request.get_json()
        
        # Update lecture fields if provided
        if data.get('title'):
            lecture.title = data['title']
        if data.get('content'):
            lecture.content = data['content']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Lecture updated successfully',
            'lecture': lecture.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'message': 'Failed to update lecture', 'error': str(e)}), 500

@lectures_bp.route('/api/lectures/<int:lecture_id>', methods=['DELETE'])
def delete_lecture(lecture_id):
    try:
        lecture = Lecture.query.get(lecture_id)
        if not lecture:
            return jsonify({'message': 'Lecture not found'}), 404
        
        db.session.delete(lecture)
        db.session.commit()
        
        return jsonify({'message': 'Lecture deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to delete lecture', 'error': str(e)}), 500