# Привет, я Руслан 👋
Python разработчик, в поиске работы, люблю писать код.
Сейчас работаю в компании MindFusion Backend Разработчиком.

<p align='center'>
   <a href="https://github-readme-stats.vercel.app/api?username=s1ntecs&show_icons=true&count_private=true"><img
           height=150
           src="https://github-readme-stats.vercel.app/api?username=s1ntecs&show_icons=true&count_private=true"/></a>
   <a href="https://github.com/s1ntecs/github-readme-stats"><img height=150
                                                                  src="https://github-readme-stats.vercel.app/api/top-langs/?username=s1ntecs&layout=compact"/></a>
</p>

<p align='center'>
   </a>
   <a href="https://t.me/sintecs">
       <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
   </a>
<p align='center'>
   📫 Мое резюме в HH <a href='https://almetyevsk.hh.ru/resume/95387935ff0b16b6d60039ed1f575264476257'>Руслан Фаттахов</a>
</p>
   
<p align='center'>
   📫 Моя почта <a href='mailto:s1ntecs@icloud.com'>s1ntecs@icloud.com</a>
</p>

## 🛠 Мой стэк технологий:
*   Python 
*   Django Framework, DRF, FastAPI, Aiohttp, aiogram
*   MySQL, PostgreSQL, MongoDB, RabbitMQ
*   selenium, BeatifulSoup, Google API, pytest
*   Linux, GitHub, Docker, Docker-dompose
*   Яндекс.Облако, AWS Buckets



# Тестовое задание junior python developer
## Время на выполнение: 4-6 часов

Стек: Python3, Asyncio, MongoDB, любая асинхронная библиотека для телеграм бота


Приоритетным является решение через построение запросов к mongodb


Описание задачи:

Вашей задачей в рамках этого тестового задания будет написание алгоритма агрегации статистических данных о зарплатах сотрудников компании по временным промежуткам. Ссылка на скачивание коллекции со статистическими данными, которую необходимо использовать при выполнении задания, находится в конце документа.


На обычном языке пример задачи выглядит следующим образом: “Необходимо посчитать суммы всех выплат с {28.02.2022} по {31.03.2022}, единица группировки - {день}”.
Ваш алгоритм должен принимать на вход:
Дату и время старта агрегации в ISO формате (далее dt_from)
Дату и время окончания агрегации в ISO формате (далее dt_upto)
Тип агрегации (далее group_type). Типы агрегации могут быть следующие: hour, day, month. То есть группировка всех данных за час, день, неделю, месяц.

Пример входных данных:
```
{
"dt_from":"2022-09-01T00:00:00",
"dt_upto":"2022-12-31T23:59:00",
"group_type":"month"
} 
```
Пример ответа:
```
{"dataset": [5906586, 5515874, 5889803, 6092634], "labels": ["2022-09-01T00:00:00", "2022-10-01T00:00:00", "2022-11-01T00:00:00", "2022-12-01T00:00:00"]}
```
