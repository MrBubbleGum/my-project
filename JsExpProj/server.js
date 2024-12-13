const http = require('http');

// Порт, на котором будет работать сервер
const PORT = 3000;

// Создание сервера
const server = http.createServer((req, res) => {
    // Установка заголовка ответа
    res.setHeader('Content-Type', 'application/json');

    // Обработка различных типов запросов
    if (req.method === 'GET') {
        res.statusCode = 200;
        res.end(JSON.stringify({ message: 'Это ответ на GET запрос' }));
    } else if (req.method === 'POST') {
        let body = '';
        
        req.on('data', chunk => {
            body += chunk.toString(); // Преобразуем Buffer в строку
        });

        req.on('end', () => {
            res.statusCode = 200;
            res.end(JSON.stringify({ message: 'Это ответ на POST запрос', data: body }));
        });
    } else {
        res.statusCode = 405; // Метод не разрешен
        res.end(JSON.stringify({ error: 'Метод не поддерживается' }));
    }
});

// Запускаем сервер
server.listen(PORT, () => {
    console.log(`Сервер запущен на http://localhost:${PORT}`);
});