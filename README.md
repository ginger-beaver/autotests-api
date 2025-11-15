# API Automation Tests

Реализация набора тестов для проверки функциональности API сервера.
Тесты написаны с использованием **Python**, **Pytest**, **Allure**, **Pydantic**, **Faker** и **HTTPX**. 
Исходный код приложения доступен на [GitHub](https://github.com/Nikita-Filonov/qa-automation-engineer-api-course).

## Описание проекта

Цель — автоматизация тестирования REST API приложения.  
Проект проверяет корректность работы различных эндпоинтов и реализует лучшие практики тестовой автоматизации:

- API-клиенты для структурированной работы с эндпоинтами
- **Pytest**-фикстуры для подготовки переиспользуемого тестового окружения
- **Pydantic**-схемы для строгой валидации данных
- Генерация фейковых данных с **Faker**
- **Allure** для визуализации отчетов
- Интеграция с CI/CD-платформой **GitHub Actions** — на каждом **push** или **pull request** автоматически запускаются
  тесты, формируется отчет и
  публикуется на [**GitHub Pages**](https://ginger-beaver.github.io/autotests-api/)

## Установка и запуск

Клонируйте репозиторий:

```bash
git clone https://github.com/ginger-beaver/autotests-api
cd autotests-api
```

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

## Запуск тестов с генерацией Allure отчета

Эта команда выполнит все тесты и покажет результат в терминале:

```bash
pytest -m "regression" --alluredir=./allure-results
```

## Просмотр Allure отчета

Эта команда откроет отчет в вашем браузере:

```bash
allure serve allure-results
```
