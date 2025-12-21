"""
Script to initialize the database
"""

import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__)))

from app import create_app
from utils.db_init import init_db

def main():
    app = create_app()
    with app.app_context():
        init_db(app)
        print("Database initialized successfully!")

if __name__ == "__main__":
    main()