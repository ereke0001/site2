from flask import Blueprint, request, jsonify
import subprocess
import sys
import io
import contextlib
import traceback

compiler_bp = Blueprint('compiler', __name__)

@compiler_bp.route('/api/compiler/execute', methods=['POST'])
def execute_code():
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        if not code:
            return jsonify({'message': 'Code is required'}), 400
        
        # Execute the code in a restricted environment
        output = execute_python_code(code)
        
        return jsonify({
            'success': True,
            'output': output
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

def execute_python_code(code):
    """
    Execute Python code and return the output
    """
    # Create a string buffer to capture stdout
    buffer = io.StringIO()
    
    # Redirect stdout to our buffer
    with contextlib.redirect_stdout(buffer):
        try:
            # Execute the code
            exec(code, {})
        except Exception as e:
            # Capture exceptions
            traceback.print_exc(file=buffer)
    
    # Get the output from the buffer
    output = buffer.getvalue()
    return output