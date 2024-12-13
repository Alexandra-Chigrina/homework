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

запустите скрипты из модуля main.py в корне репозитория
```commandline
python main.py
```


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
