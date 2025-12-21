import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';

// Import components
import Header from './components/Header';

// Import pages
import Home from './pages/Home';
import Lectures from './pages/Lectures';
import LectureDetail from './pages/LectureDetail';
import Tests from './pages/Tests';
import TestDetail from './pages/TestDetail';
import Videos from './pages/Videos';
import Compiler from './pages/Compiler';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-white flex flex-col">
        <Header />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/lectures" element={<Lectures />} />
            <Route path="/lectures/:id" element={<LectureDetail />} />
            <Route path="/tests" element={<Tests />} />
            <Route path="/tests/:id" element={<TestDetail />} />
            <Route path="/videos" element={<Videos />} />
            <Route path="/compiler" element={<Compiler />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;