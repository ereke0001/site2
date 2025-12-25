import React from 'react';

const Videos = () => {
  const videos = [
    {
      id: 1,
      title: "Python с нуля за 1 час",
      description: "Быстрое и понятное введение в Python для начинающих",
      thumbnail: "https://img.youtube.com/vi/kqtD5dpn9C8/maxresdefault.jpg",
      url: "https://www.youtube.com/watch?v=kqtD5dpn9C8"
    },
    {
      id: 2,
      title: "Переменные и типы данных в Python",
      description: "Разбор переменных, чисел, строк и списков в Python",
      thumbnail: "https://img.youtube.com/vi/khKv-8q7YmY/maxresdefault.jpg",
      url: "https://www.youtube.com/watch?v=khKv-8q7YmY"
    },
    {
      id: 3,
      title: "Условные операторы и циклы в Python",
      description: "if, else, for, while — основы управления потоком программы",
      thumbnail: "https://img.youtube.com/vi/6iF8Xb7Z3wQ/maxresdefault.jpg",
      url: "https://www.youtube.com/watch?v=6iF8Xb7Z3wQ"
    }
  ];

  return (
    <div className="container mx-auto px-4 py-8">
      <header className="mb-8 pb-4 border-b">
        <h1 className="text-3xl font-bold mb-2">Видеоуроки по Python</h1>
        <p className="text-gray-600">
          Смотрите нашу коллекцию видеоуроков по программированию на Python
        </p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {videos.map((video) => (
          <div key={video.id} className="card p-4 rounded-xl shadow">
            <div className="aspect-video bg-gray-200 mb-4 overflow-hidden rounded-lg">
              <img
                src={video.thumbnail}
                alt={video.title}
                className="w-full h-full object-cover"
              />
            </div>
            <h3 className="text-xl font-semibold mb-2">{video.title}</h3>
            <p className="text-gray-600 mb-4">{video.description}</p>
            <a
              href={video.url}
              target="_blank"
              rel="noopener noreferrer"
              className="btn btn-primary inline-block"
            >
              Смотреть видео
            </a>
          </div>
        ))}
      </div>

      <div className="card mt-8 p-6 rounded-xl shadow">
        <h2 className="text-2xl font-bold mb-4">О нашем видеоконтенте</h2>
        <p className="mb-4">
          Наши видеоуроки охватывают широкий спектр тем по Python — от основ для
          начинающих до более продвинутых концепций.
        </p>
        <p>
          Видео размещены на YouTube, вы можете смотреть их в удобное время и
          возвращаться к нужным темам.
        </p>
      </div>
    </div>
  );
};

export default Videos;
