import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import apiClient from '../config/api';

const TestDetail = () => {
  const { id } = useParams();
  const [test, setTest] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [answers, setAnswers] = useState([]);
  const [submitted, setSubmitted] = useState(false);
  const [result, setResult] = useState(null);
  const [studentName, setStudentName] = useState('');

  useEffect(() => {
    fetchTest();
  }, [id]);

  const fetchTest = async () => {
    try {
      const response = await apiClient.get(`/api/tests/${id}`);
      setTest(response.data.test);
      // Initialize answers array
      setAnswers(new Array(response.data.test.questions?.length || 0).fill(null));
    } catch (err) {
      setError(err.response?.data?.message || 'Не удалось загрузить тест');
    } finally {
      setLoading(false);
    }
  };

  const handleAnswerChange = (questionIndex, optionIndex) => {
    const newAnswers = [...answers];
    newAnswers[questionIndex] = optionIndex;
    setAnswers(newAnswers);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Check if name is provided
    if (!studentName.trim()) {
      alert('Пожалуйста, введите ваше имя перед отправкой теста.');
      return;
    }
    
    // Check if all questions are answered
    if (answers.some(answer => answer === null)) {
      alert('Пожалуйста, ответьте на все вопросы перед отправкой.');
      return;
    }
    
    try {
      const response = await apiClient.post(`/api/tests/${id}/submit`, {
        name: studentName.trim(),
        answers
      });
      
      setResult(response.data);
      setSubmitted(true);
    } catch (err) {
      setError(err.response?.data?.message || 'Не удалось отправить тест');
    }
  };

  if (loading) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="card">
          <p>Загрузка теста...</p>
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
          <Link to="/tests" className="btn btn-secondary mt-4">
            Назад к тестам
          </Link>
        </div>
      </div>
    );
  }

  if (!test) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="card">
          <p>Тест не найден.</p>
          <Link to="/tests" className="btn btn-secondary mt-4">
            Назад к тестам
          </Link>
        </div>
      </div>
    );
  }

  if (submitted && result) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="card">
          <h1 className="text-3xl font-bold mb-6">Результаты теста</h1>
          
          {result.student_name && (
            <div className="mb-4 pb-4 border-b">
              <p className="text-lg">
                <strong>Имя:</strong> {result.student_name}
              </p>
            </div>
          )}
          
          <div className="text-center mb-8">
            <div className="text-6xl font-bold text-gray-800 mb-2">
              {result.score}%
            </div>
            <p className="text-xl">
              Вы ответили правильно на {result.correct_answers} из {result.total_questions} вопросов
            </p>
          </div>
          
          <div className="bg-gray-100 p-4 border mb-6">
            <h2 className="text-xl font-semibold mb-2">Сводка результатов</h2>
            <div className="space-y-2">
              <div className="flex justify-between">
                <span>Всего вопросов:</span>
                <span>{result.total_questions}</span>
              </div>
              <div className="flex justify-between">
                <span>Правильных ответов:</span>
                <span>{result.correct_answers}</span>
              </div>
              <div className="flex justify-between">
                <span>Неправильных ответов:</span>
                <span>{result.total_questions - result.correct_answers}</span>
              </div>
              <div className="flex justify-between font-semibold">
                <span>Оценка:</span>
                <span>{result.score}%</span>
              </div>
            </div>
          </div>
          
          <div className="flex gap-4">
            <Link to="/tests" className="btn btn-secondary">
              Назад к тестам
            </Link>
            <button 
              onClick={() => {
                setSubmitted(false);
                setResult(null);
                setStudentName('');
                // Reset answers
                setAnswers(new Array(test.questions?.length || 0).fill(null));
              }}
              className="btn btn-primary"
            >
              Пройти тест заново
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-6">
        <Link to="/tests" className="text-gray-600 hover:text-gray-800">
          ← Назад к тестам
        </Link>
      </div>

      <div className="card">
        <h1 className="text-3xl font-bold mb-2">{test.title}</h1>
        <div className="text-sm text-gray-500 mb-6">
          Создано: {new Date(test.created_at).toLocaleDateString()}
        </div>
        
        <form onSubmit={handleSubmit}>
          <div className="mb-6 pb-6 border-b">
            <label className="form-label" htmlFor="student-name">
              Ваше имя
            </label>
            <input
              id="student-name"
              type="text"
              value={studentName}
              onChange={(e) => setStudentName(e.target.value)}
              className="form-input"
              placeholder="Введите ваше имя"
              required
            />
          </div>
          <div className="space-y-8">
            {test.questions?.map((question, qIndex) => (
              <div key={qIndex} className="border-b pb-6">
                <h3 className="text-lg font-semibold mb-4">
                  {qIndex + 1}. {question.question}
                </h3>
                
                <div className="space-y-2">
                  {question.options?.map((option, oIndex) => (
                    <label key={oIndex} className="flex items-start">
                      <input
                        type="radio"
                        name={`question-${qIndex}`}
                        checked={answers[qIndex] === oIndex}
                        onChange={() => handleAnswerChange(qIndex, oIndex)}
                        className="mt-1 mr-3"
                      />
                      <span>{option}</span>
                    </label>
                  ))}
                </div>
              </div>
            ))}
          </div>
          
          <div className="mt-8">
            <button type="submit" className="btn btn-primary">
              Отправить тест
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default TestDetail;