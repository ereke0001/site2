import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {

  return (
    <header className="header">
      <div className="container mx-auto px-4">
        <div className="flex justify-between items-center">
          <Link to="/" className="text-xl font-bold">
            Python Course
          </Link>
          
          <nav>
            <div className="flex items-center space-x-4">
              <Link to="/" className="nav-link">Главная</Link>
              <Link to="/lectures" className="nav-link">Лекции</Link>
              <Link to="/tests" className="nav-link">Тесты</Link>
              <Link to="/videos" className="nav-link">Видео</Link>
              <Link to="/compiler" className="nav-link">Компилятор</Link>
            </div>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;