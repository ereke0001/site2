import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify
from flask_cors import CORS
from asgiref.wsgi import WsgiToAsgi
from config import Config
from models import db
from utils.db_init import init_db
from routes.lectures import lectures_bp
from routes.tests import tests_bp
from routes.compiler import compiler_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Enable CORS for all routes
    CORS(app)
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(lectures_bp)
    app.register_blueprint(tests_bp)
    app.register_blueprint(compiler_bp)
    
    # Initialize database
    with app.app_context():
        init_db(db, app)
    
    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health_check():
        return jsonify({'status': 'healthy', 'message': 'Python Course API is running'})
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'message': 'Endpoint not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'message': 'Internal server error'}), 500
    
    return app

# Create Flask app
flask_app = create_app()

# Wrap Flask WSGI app with ASGI wrapper for uvicorn
app = WsgiToAsgi(flask_app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)