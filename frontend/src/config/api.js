import axios from 'axios';

// Ngrok URL для бекенда
const API_BASE_URL = 'https://unsoundly-expropriable-yvette.ngrok-free.dev';

// Создаем экземпляр axios с базовым URL
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
    'ngrok-skip-browser-warning': 'true',
  }
});

export default apiClient;

