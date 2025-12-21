import React, { useState } from 'react';
import apiClient from '../config/api';

const Compiler = () => {
  const [code, setCode] = useState('# Напишите ваш код здесь\nprint("Привет, мир!")');
  const [output, setOutput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const executeCode = async () => {
    try {
      setIsLoading(true);
      setError('');
      setOutput('');
      
      const response = await apiClient.post('/api/compiler/execute', { code });
      
      if (response.data.success) {
        setOutput(response.data.output);
      } else {
        setError(response.data.error);
      }
    } catch (err) {
      setError('Ошибка при выполнении кода: ' + (err.response?.data?.error || err.message));
    } finally {
      setIsLoading(false);
    }
  };

  const clearOutput = () => {
    setOutput('');
    setError('');
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <header className="mb-8 pb-4 border-b">
        <h1 className="text-3xl font-bold mb-2">Python Компилятор</h1>
        <p className="text-gray-600">Пишите и выполняйте код Python прямо в браузере</p>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="card">
          <h2 className="text-2xl font-bold mb-4">Редактор кода</h2>
          <textarea
            value={code}
            onChange={(e) => setCode(e.target.value)}
            className="w-full h-64 font-mono text-sm p-4 border"
            placeholder="Введите ваш Python код здесь..."
          />
          <div className="flex gap-4 mt-4">
            <button 
              onClick={executeCode}
              disabled={isLoading}
              className="btn btn-primary"
            >
              {isLoading ? 'Выполняется...' : 'Выполнить код'}
            </button>
            <button 
              onClick={clearOutput}
              className="btn btn-secondary"
            >
              Очистить вывод
            </button>
          </div>
        </div>

        <div className="card">
          <h2 className="text-2xl font-bold mb-4">Результат выполнения</h2>
          <div className="bg-gray-900 text-green-400 font-mono text-sm p-4 h-64 overflow-auto border">
            {output && <pre>{output}</pre>}
            {error && <pre className="text-red-400">{error}</pre>}
            {!output && !error && !isLoading && (
              <p className="text-gray-500">Результат выполнения кода появится здесь...</p>
            )}
            {isLoading && <p className="text-gray-500">Выполнение кода...</p>}
          </div>
        </div>
      </div>

      <div className="card mt-6">
        <h2 className="text-2xl font-bold mb-4">Как использовать</h2>
        <ul className="list-disc pl-6 space-y-2">
          <li>Введите Python код в редактор слева</li>
          <li>Нажмите кнопку "Выполнить код" для запуска программы</li>
          <li>Результат выполнения появится в правой панели</li>
          <li>Используйте кнопку "Очистить вывод" для очистки результатов</li>
        </ul>
        
        <h3 className="text-xl font-semibold mt-6 mb-3">Примеры кода:</h3>
        <div className="bg-gray-100 p-4 border font-mono text-sm">
          <p># Простой вывод</p>
          <p className="mb-2">print("Привет, мир!")</p>
          
          <p># Математические операции</p>
          <p className="mb-2">print(2 + 3 * 4)</p>
          
          <p># Цикл</p>
          <p className="mb-2">for i in range(5):</p>
          <p className="ml-4 mb-2">print(f"Число: {'{'}i{'}'}")</p>
          
          <p># Функция</p>
          <p className="mb-2">def greet(name):</p>
          <p className="ml-4 mb-2">return f"Привет, {'{'}name{'}'}!"</p>
          <p className="mb-2">print(greet("Пользователь"))</p>
        </div>
      </div>
    </div>
  );
};

export default Compiler;