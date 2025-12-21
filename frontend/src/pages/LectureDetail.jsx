import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

const LectureDetail = () => {
  const { id } = useParams();
  const [lecture, setLecture] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchLecture();
  }, [id]);

  const fetchLecture = async () => {
    try {
      const response = await axios.get(`/api/lectures/${id}`);
      setLecture(response.data.lecture);
    } catch (err) {
      setError(err.response?.data?.message || 'Не удалось загрузить лекцию');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="card">
          <p>Загрузка лекции...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="card">
          <div className="alert alert-error">
            {error}
          </div>
          <Link to="/lectures" className="btn btn-secondary mt-4">
            Назад к лекциям
          </Link>
        </div>
      </div>
    );
  }

  if (!lecture) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="card">
          <p>Лекция не найдена.</p>
          <Link to="/lectures" className="btn btn-secondary mt-4">
            Назад к лекциям
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-6">
        <Link to="/lectures" className="text-gray-600 hover:text-gray-800">
          ← Назад к лекциям
        </Link>
      </div>

      <div className="card">
        <h1 className="text-3xl font-bold mb-4">{lecture.title}</h1>
        <div className="text-sm text-gray-500 mb-6">
          Создано: {new Date(lecture.created_at).toLocaleDateString()}
        </div>
        
        <div 
          className="prose max-w-none"
          dangerouslySetInnerHTML={{ __html: lecture.content }}
        />
      </div>
    </div>
  );
};

export default LectureDetail;