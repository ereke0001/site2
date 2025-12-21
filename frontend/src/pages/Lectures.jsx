import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const Lectures = () => {
  const [lectures, setLectures] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchLectures();
  }, []);

  const fetchLectures = async () => {
    try {
      const response = await axios.get('/api/lectures');
      setLectures(response.data.lectures);
    } catch (err) {
      setError(err.response?.data?.message || 'Не удалось загрузить лекции');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="card">
          <p>Загрузка лекций...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <header className="mb-8 pb-4 border-b">
        <h1 className="text-3xl font-bold mb-2">Лекции по Python</h1>
        <p className="text-gray-600">Просмотрите нашу коллекцию лекций по программированию на Python</p>
      </header>

      {error && (
        <div className="alert alert-error mb-6">
          {error}
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {lectures.map((lecture) => (
          <Link 
            to={`/lectures/${lecture.id}`} 
            key={lecture.id}
            className="card"
          >
            <h3 className="text-xl font-semibold mb-2">{lecture.title}</h3>
            <div 
              className="text-gray-600 prose max-w-none"
              dangerouslySetInnerHTML={{ __html: lecture.content.substring(0, 150) + '...' }}
            />
            <div className="mt-4 text-sm text-gray-500">
              Создано: {new Date(lecture.created_at).toLocaleDateString()}
            </div>
          </Link>
        ))}
      </div>

      {lectures.length === 0 && !loading && (
        <div className="card text-center">
          <p>На данный момент лекции недоступны.</p>
        </div>
      )}
    </div>
  );
};

export default Lectures;