# Тестовое задание "WEB - приложение для определения заполненных форм"

## Описание

Сопоставление названий полей формы и типов данных между данными 
от пользователя поступающих в систему в рамках Post - запроса
и информацией хранимой в базде данных на сервере с последующей 
валидацией данных.  
Вывод информации о совпавших формах, в случае если данные из  
Post - запроса  прошли вадиданию данных, либо об отсутствии 
совпадающих форм, либо о тех данных, которые не смогли пройти 
валидацию.


## Инструкция по установке

- Склонировать репозиторий
```
git clone https://github.com/edick2081n/filling/tree/master/filling
```


- Переходим в папку проекта  
Формируем и активируем виртуальное окружение, устанавливаем зависимости
```bash
cd filling
py - 3.9 - m venv virtualenv\filling
virtualenv\filling\Scripts\activate
pip install -r requirements.txt
 
```
- Запуск тестов
```bash
python manage.py test

```
- Запуск в режиме разработки (опционально)
```bach
python manage.py runserver
```
