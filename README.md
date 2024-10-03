# QRkot_spreadseets

# Оглавление
- [:page_with_curl: Описание](https://github.com/Tiaki026/QRkot_spreadsheets/blob/master/README.md#page_with_curl-описание)
- [:wrench:Процесс разработки, особенности и трудности](https://github.com/Tiaki026/QRkot_spreadsheets/blob/master/README.md#wrench-процесс-разработки-особенности-и-трудности)
  - [Было изучено](https://github.com/Tiaki026/QRkot_spreadsheets/blob/master/README.md#было-изучено)
  - [Трудности возникшие в работе](https://github.com/Tiaki026/QRkot_spreadsheets/blob/master/README.md#трудности-возникшие-в-работе)
- [:computer: Стек технологий](https://github.com/Tiaki026/QRkot_spreadsheets/blob/master/README.md#computer-стек-технологий)
- [:page_with_curl: Как воспользоваться проектом](https://github.com/Tiaki026/QRkot_spreadsheets/blob/master/README.md#page_with_curl-как-воспользоваться-проектом)
  - [Подготовка проекта](https://github.com/Tiaki026/QRkot_spreadsheets/blob/master/README.md#подготовка-проекта)
  - [Работа с проектом](https://github.com/Tiaki026/QRkot_spreadsheets/blob/master/README.md#работа-с-проектом)
- [Автор](https://github.com/Tiaki026/QRkot_spreadsheets/blob/master/README.md#автор)
## :page_with_curl: Описание
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

<details>
<summary>:mag: Спойлер</summary>
  
![image](https://github.com/user-attachments/assets/198d4361-f5d3-4b5d-9723-7729425be36e)

</details>

### Проекты
В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.
Реализованы отчеты на гугл диск.

<details>
<summary>:mag: Спойлер</summary>
  
  ![image](https://github.com/user-attachments/assets/71578eaf-5210-447b-87f1-b7110f1dfdb4)

</details>

### Пожертвования
Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

### Пользователи
Целевые проекты и отчеты создаются администраторами сайта. 
Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых.
Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.

## :wrench: Процесс разработки, особенности и трудности

### Было изучено:
- FastApi:  Современный веб-фреймворк для создания API на Python.
            Быстрый, асинхронный, поддерживает автоматическую генерацию OpenAPI документации и валидацию 
            данных с использованием Pydantic. Часто используется для создания производительных REST и GraphQL API.
- Alembic:  Инструмент для управления миграциями базы данных.
            Позволяет отслеживать изменения в структуре базы данных (например, добавление таблиц 
            или изменение колонок) и применять их в разных окружениях, поддерживая версионность схемы базы.
- Pydantic: Библиотека для управления данными и их валидации. 
            Позволяет определять Python-модели (схемы) с проверкой типов и значений данных, что делает её 
            полезной для работы с входными и выходными данными, особенно в FastAPI.
- SQLAlchemy: ORM (Object Relational Mapper) для работы с реляционными базами данных. 
            Предоставляет удобный интерфейс для работы с базами данных, позволяя писать запросы на Python 
            вместо SQL, и поддерживает как декларативные модели (ORM), так и чистые SQL-запросы.
- Google Sheets API: позволяет программно взаимодействовать с Google Таблицами. Используя этот API, 
            можно создавать, обновлять, читать и изменять содержимое таблиц. Он позволяет автоматизировать задачи, 
            такие как генерация отчётов, обновление данных и управление таблицами через сторонние приложения.
- Google Drive API: предоставляет доступ к файлам, хранящимся в Google Диске, включая управление 
          файлами и папками. С его помощью можно загружать, удалять, находить файлы, а также управлять правами доступа.

> 
> Решил добавить поиск всех отчетов на диске и уделение старых отчетов (кроме последнего)
> 

### Трудности возникшие в работе
В этот раз без трудностей!

## :computer: Стек технологий
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![SQLAlchemy](https://camo.githubusercontent.com/002ee4ca516670df2b07f9fead4c132c71b7f367002ab21681a686c923c0acd6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c616c6368656d792d6662666266623f7374796c653d666f722d7468652d6261646765)
- ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
- ![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)
- ![Google Sheets](https://img.shields.io/badge/Google%20Sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white)

## :page_with_curl: Как воспользоваться проектом
### Подготовка проекта
<details>
<summary>:mag: Спойлер</summary>

1. Клонирование проекта с GitHub
```
git@github.com:Tiaki026/cat_charity_fund.git
```
2.	Создайте виртуальное окружение.

Linux
```commandline
python3 -m venv venv
```
Windows
```commandline
python -m venv venv
```
3.	Активируйте виртуальное окружение.

Linux
```commandline
source venv/bin/activate
```
Windows
```commandline
source venv/Scripts/activate
```
4.	Установите зависимости.
```commandline
pip install -r requirements.txt
```
5.	Создать миграции и применить их.
```commandline
alembic init --template async alembic
alembic revision --autogenerate -m "Your description" --rev-id 01
alembic upgrade head
```

</details>

### Работа с проектом
Запуск проекта
```commandline
uvicorn app.main:app --reload
```
Просмотр документации
```commandline
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```
## Автор:
  - [Колотиков Евгений](https://github.com/Tiaki026)
## 

  ## [:top: Путь наверх :top:](https://github.com/Tiaki026/QRkot_spreadsheets/blob/master/README.md#qrkot)
