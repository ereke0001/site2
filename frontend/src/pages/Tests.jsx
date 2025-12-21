import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import apiClient from '../config/api';

const Tests = () => {
  const [tests, setTests] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchTests();
  }, []);

  const fetchTests = async () => {
    try {
      const response = await apiClient.get('/api/tests');
      setTests(response.data.tests);
    } catch (err) {
      setError(err.response?.data?.message || 'Не удалось загрузить тесты');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="card">
          <p>Загрузка тестов...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <header className="mb-8 pb-4 border-b">
        <h1 className="text-3xl font-bold mb-2">Тесты по Python</h1>
        <p className="text-gray-600">Проверьте свои знания с помощью наших тестов по программированию на Python</p>
      </header>

      {error && (
        <div className="alert alert-error mb-6">
          {error}
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {tests.map((test) => (
          <Link 
            to={`/tests/${test.id}`} 
            key={test.id}
            className="card"
          >
            <h3 className="text-xl font-semibold mb-2">{test.title}</h3>
            <p className="text-gray-600 mb-4">
              {test.questions?.length || 0} вопросов
            </p>
            <div className="mt-4 text-sm text-gray-500">
              Создано: {new Date(test.created_at).toLocaleDateString()}
            </div>
          </Link>
        ))}
      </div>

      {tests.length === 0 && !loading && (
        <div className="card text-center">
          <p>На данный момент тесты недоступны.</p>
        </div>
      )}
    </div>
  );
};

export default Tests;