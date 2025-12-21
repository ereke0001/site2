import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="container mx-auto px-4 py-12 max-w-4xl">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold mb-4">Курс по Python</h1>
        <p className="text-lg text-gray-600">
          Изучайте программирование на Python с помощью лекций, тестов и практических заданий
        </p>
      </div>

      <div className="mb-12">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <Link to="/lectures" className="card text-center">
            <h3 className="text-lg font-semibold mb-3">Лекции</h3>
            <p className="text-sm text-gray-600">Изучайте теорию и практику программирования</p>
          </Link>
          
          <Link to="/tests" className="card text-center">
            <h3 className="text-lg font-semibold mb-3">Тесты</h3>
            <p className="text-sm text-gray-600">Проверяйте свои знания</p>
          </Link>
          
          <Link to="/compiler" className="card text-center">
            <h3 className="text-lg font-semibold mb-3">Компилятор</h3>
            <p className="text-sm text-gray-600">Выполняйте код прямо в браузере</p>
          </Link>
        </div>
      </div>

      <div className="border-t pt-8">
        <h2 className="text-2xl font-bold mb-4">О курсе</h2>
        <p className="text-gray-700 mb-4">
          Курс охватывает основы программирования на Python: от базового синтаксиса до 
          объектно-ориентированного программирования и работы с файлами.
        </p>
        <p className="text-gray-700">
          Все материалы доступны бесплатно. Начните изучение с любого раздела.
        </p>
      </div>
    </div>
  );
};

export default Home;