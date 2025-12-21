from flask import Blueprint, request, jsonify
from models import db, Test, Result, User
tests_bp = Blueprint('tests', __name__)

@tests_bp.route('/api/tests', methods=['GET'])
def get_tests():
    try:
        tests = Test.query.all()
        return jsonify({
            'tests': [test.to_dict() for test in tests]
        }), 200
    except Exception as e:
        return jsonify({'message': 'Failed to retrieve tests', 'error': str(e)}), 500

@tests_bp.route('/api/tests/<int:test_id>', methods=['GET'])
def get_test(test_id):
    try:
        test = Test.query.get(test_id)
        if not test:
            return jsonify({'message': 'Test not found'}), 404
        
        # Return test without answers for regular users
        test_data = test.to_dict()
        # Remove correct answers for security
        for question in test_data['questions']:
            if 'correct_answer' in question:
                del question['correct_answer']
        
        return jsonify({'test': test_data}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to retrieve test', 'error': str(e)}), 500

@tests_bp.route('/api/tests', methods=['POST'])
def create_test():
    try:
        data = request.get_json()
        
        # Validate input
        if not data or not data.get('title') or not data.get('questions'):
            return jsonify({'message': 'Title and questions are required'}), 400
        
        # Create new test
        test = Test(
            title=data['title'],
            questions=data['questions']
        )
        
        db.session.add(test)
        db.session.commit()
        
        return jsonify({
            'message': 'Test created successfully',
            'test': test.to_dict()
        }), 201
    except Exception as e:
        return jsonify({'message': 'Failed to create test', 'error': str(e)}), 500

@tests_bp.route('/api/tests/<int:test_id>', methods=['PUT'])
def update_test(test_id):
    try:
        test = Test.query.get(test_id)
        if not test:
            return jsonify({'message': 'Test not found'}), 404
        
        data = request.get_json()
        
        # Update test fields if provided
        if data.get('title'):
            test.title = data['title']
        if data.get('questions'):
            test.questions = data['questions']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Test updated successfully',
            'test': test.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'message': 'Failed to update test', 'error': str(e)}), 500

@tests_bp.route('/api/tests/<int:test_id>/submit', methods=['POST'])
def submit_test(test_id):
    try:
        test = Test.query.get(test_id)
        if not test:
            return jsonify({'message': 'Test not found'}), 404
        
        data = request.get_json()
        if not data or not data.get('answers'):
            return jsonify({'message': 'Answers are required'}), 400
        
        if not data.get('name') or not data['name'].strip():
            return jsonify({'message': 'Name is required'}), 400
        
        # Find or create user with the given name
        student_name = data['name'].strip()
        user = User.query.filter_by(name=student_name).first()
        
        if not user:
            # Create new user with the given name
            user = User(name=student_name)
            db.session.add(user)
            db.session.commit()
        
        answers = data['answers']
        correct_count = 0
        total_questions = len(test.questions)
        
        # Check answers
        for i, question in enumerate(test.questions):
            if i < len(answers) and answers[i] == question['correct_answer']:
                correct_count += 1
        
        # Calculate score
        score = int((correct_count / total_questions) * 100)
        
        # Save result
        result = Result(
            user_id=user.id,
            test_id=test.id,
            score=score
        )
        
        db.session.add(result)
        db.session.commit()
        
        return jsonify({
            'message': 'Test submitted successfully',
            'score': score,
            'correct_answers': correct_count,
            'total_questions': total_questions,
            'student_name': student_name
        }), 200
    except Exception as e:
        return jsonify({'message': 'Failed to submit test', 'error': str(e)}), 500

@tests_bp.route('/api/results', methods=['GET'])
def get_user_results():
    try:
        # Use default user
        user = User.query.first()
        if not user:
            return jsonify({'message': 'User not found'}), 404
        
        results = Result.query.filter_by(user_id=user.id).all()
        return jsonify({
            'results': [result.to_dict() for result in results]
        }), 200
    except Exception as e:
        return jsonify({'message': 'Failed to retrieve results', 'error': str(e)}), 500