# Running the Python Course Application

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

## Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

5. Run the Flask application with uvicorn:
   ```
   python run.py
   ```
   or directly:
   ```
   uvicorn app:app --host 0.0.0.0 --port 5000 --reload
   ```

   The backend will be available at http://localhost:5000

## Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install the required Node.js packages:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm run dev
   ```

   The frontend will be available at http://localhost:3000

## Доступ к контенту

Приложение не требует регистрации или входа в систему. Все материалы доступны сразу после запуска.

## API Endpoints

### Лекции
- GET /api/lectures - Get all lectures
- GET /api/lectures/<id> - Get a specific lecture


### Тесты
- GET /api/tests - Получить все тесты
- GET /api/tests/<id> - Получить конкретный тест
- POST /api/tests/<id>/submit - Отправить ответы на тест
- GET /api/results - Получить результаты тестов

### Компилятор
- POST /api/compiler/execute - Выполнить Python код