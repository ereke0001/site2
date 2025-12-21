# Python Course Website

Educational website for learning Python with interactive lectures, tests, and video lessons.

## Project Structure

```
python-course/
│
├── backend/
│   ├── app.py
│   ├── db.sqlite3
│   ├── models.py
│   ├── config.py
│   ├── routes/
│   │   ├── lectures.py
│   │   ├── tests.py
│   │   └── compiler.py
│   └── utils/
│       ├── db_init.py
│
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   ├── pages/
│   │   └── styles/
│
└── README.md
```

## Features

- Interactive Python lectures
- Knowledge tests
- Video lessons
- Интерактивные лекции по Python
- Тесты для проверки знаний
- Видеоуроки
- Онлайн компилятор Python

## Technologies

- Backend: Flask (Python)
- Frontend: React.js
- Database: SQLite
- REST API for frontend-backend communication

## Getting Started

For detailed instructions on how to run the application, please see [RUNNING.md](RUNNING.md).

### Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

### Quick Start

1. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python app.py
   ```

2. Set up the frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

### Доступ к контенту

Приложение не требует регистрации или входа в систему. Все материалы доступны сразу после запуска.

## API Documentation

See [RUNNING.md](RUNNING.md) for detailed API endpoints.