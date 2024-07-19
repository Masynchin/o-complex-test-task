# Тестовое задание Python Developer 

Сделать web приложение, оно же сайт, где пользователь вводит название города,
и получает прогноз погоды в этом городе на ближайшее время.

## Использованные технологии

*Выписать*

## Как запустить

Предварительно скачайте репозиторий:

~~~shell
git clone https://github.com/Masynchin/o-complex-test-task.git .
cd o-complex-test-task
~~~

- Через Докер

Соберите образ проекта и запустите контейнер:

~~~shell
docker build --tag o-complex-test-task .
docker run --rm --publish 8080:8080 o-complex-test-task
~~~

После этого сайт доступен по адресу `http://0.0.0.0:8080`

- Вручную

Создайте виртуальное окружение:

~~~shell
python -m venv venv
source venv/bin/activate
~~~

Поставьте зависимости проекта и запустите:

~~~shell
pip install -r requirements.txt
fastapi run main.py --port 8080
~~~

После этого сайт доступен по адресу `http://0.0.0.0:8080`

## ТЗ

- Вывод данных (прогноза погоды) должен быть в удобно читаемом формате. 
- Веб фреймворк можно использовать любой.
- api для погоды: https://open-meteo.com/ (можно использовать какое-нибудь другое, если вам удобнее)

## Бонус

- [ ] написаны тесты
- [x] всё это помещено в докер контейнер
- [x] сделаны автодополнение (подсказки) при вводе города
- [ ] при повторном посещении сайта будет предложено посмотреть погоду в городе, в котором пользователь уже смотрел ранее
- [x] будет сохраняться история поиска для каждого пользователя, и будет API, показывающее сколько раз вводили какой город
