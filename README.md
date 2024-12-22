# **Homework**


## **Описание**:

Проект 'Homework' - это виджет, который показывает несколько последних успешных банковских операций клиента.



## **Установка**:

1. Клонируйте репозиторий 
```
git clone git@github.com:Alexandra-Chigrina/homework.git
```
2. В терминале инициализируйте Poetry и активируйте виртуальное окружение
```
poetry init
poetry shell
```
3. Установите зависимости
```
pip install -r requirements.txt
```


## **Использование**:

1. запустите скрипты из модуля main.py в корне репозитория
```commandline
python main.py
```
2. В модуле src/generators.py реализованы следующие функцииЖ
    - filter_by_currency - функция фильтрации данных по заданной валюте;
    - transaction_descriptions - функция, возвращающая описание каждой операции;
    - card_number_generator - функция-генератор номеров банковских карт.

## **Примеры работы**:

- пример работы функции filter_by_state (со статусом по умолчанию 'EXECUTED'):
[
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]

- пример работы функции (сортировка по убыванию, т. е. сначала самые последние операции):
[
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]

- пример работы функциии transaction_descriptions:
```commandline
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
```
    Результат:

    Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
    
- пример работы функции card_number_generator:
```commandline
for card_number in card_number_generator(1, 5):
    print(card_number
```
    Результат:    

    0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005


## **Тестирование**

1. Установите pytest через Poetry
```
poetry add --group dev pytest
```
2. Запустить тестрование можно из модулей 'test_name', находящихся в папке 'tests' или в терминале
```
pytest
```
3. Для анализа покрытия кода тестами установите библиотеку 'pytest-cov'
```commandline
poetry add --group dev pytest-cov
```
4. Запустите тесты с оценкой покрытия
```commandline
pytest --cov=src --cov-report=term-missing tests/
```
