import React from 'react';

const Videos = () => {
  // Пример видеоданных - в реальном приложении это будет приходить из API
  const videos = [
    {
      id: 1,
      title: "Введение в Python",
      description: "Изучите основы языка программирования Python",
      thumbnail: "https://img.youtube.com/vi/sample1/maxresdefault.jpg",
      url: "https://www.youtube.com/watch?v=sample1"
    },
    {
      id: 2,
      title: "Переменные и типы данных в Python",
      description: "Понимание переменных и типов данных в Python",
      thumbnail: "https://img.youtube.com/vi/sample2/maxresdefault.jpg",
      url: "https://www.youtube.com/watch?v=sample2"
    },
    {
      id: 3,
      title: "Управляющие конструкции в Python",
      description: "Изучите условные операторы, циклы и поток управления",
      thumbnail: "https://img.youtube.com/vi/sample3/maxresdefault.jpg",
      url: "https://www.youtube.com/watch?v=sample3"
    }
  ];

  return (
    <div className="container mx-auto px-4 py-8">
      <header className="mb-8 pb-4 border-b">
        <h1 className="text-3xl font-bold mb-2">Видеоуроки по Python</h1>
        <p className="text-gray-600">Смотрите нашу коллекцию видеоуроков по программированию на Python</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {videos.map((video) => (
          <div key={video.id} className="card">
            <div className="aspect-video bg-gray-200 mb-4 overflow-hidden">
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

      <div className="card mt-8">
        <h2 className="text-2xl font-bold mb-4">О нашем видеоконтенте</h2>
        <p className="mb-4">
          Наши видеоуроки охватывают широкий спектр тем по Python, от основ для начинающих до 
          продвинутых концепций. Каждое видео тщательно подготовлено, чтобы предоставить четкие объяснения и 
          практические примеры.
        </p>
        <p>
          Видео размещены на YouTube для лучшего просмотра. Вы можете смотреть их в своем 
          темпе и возвращаться к концепциям по мере необходимости.
        </p>
      </div>
    </div>
  );
};

export default Videos;