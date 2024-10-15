import sqlalchemy as db
from sqlalchemy import Table, insert, delete, select
from datetime import datetime
import numpy as np


# Создание соединения и метаданных
engine = db.create_engine('sqlite:///myDatabase.db')
conn = engine.connect()
metadata = db.MetaData()

# Определение таблиц
Registration_data = db.Table('Registration_data', metadata, autoload_with=engine)
Aplicant = db.Table('Aplicant', metadata, autoload_with=engine)
Employer = db.Table('Employer', metadata, autoload_with=engine)

# Функция для вставки данных в Registration_data
def insert_registration(id, data_reg):
    hash_key = ""
    hash_int = np.random.randint(33, 127, 8)
    for i in range(8):
        hash_key = hash_key + chr(int(hash_int[i]))
    print("insert", hash_key)
    query = insert(Registration_data).values(id=id, hash_key=hash_key, data_reg=data_reg)
    conn.execute(query)

# Функция для вставки данных в Applicant
def insert_aplicant(data):
    query = insert(Aplicant).values(**data)
    conn.execute(query)

# Функция для вставки данных в Employer
def insert_employer(data):
    query = insert(Employer).values(**data)
    conn.execute(query)

# Функция для удаления записи из Registration_data по id
def delete_registration(registration_id):
    query = delete(Registration_data).where(Registration_data.c.id == registration_id)
    conn.execute(query)

# Функция для выбора всех записей из Registration_data
def select_all_registration():
    query = select(Registration_data)
    result = conn.execute(query).fetchall()
    return result

def select_registration(registration_id):
    query = select(Registration_data).where(Registration_data.c.id == registration_id)
    result = conn.execute(query).fetchall()
    return result

# Функция для выбора всех записей из Applicant по id регистрации
def select_aplicant_by_registration_id(registration_id):
    query = select(Aplicant).where(Aplicant.c.id == registration_id)
    result = conn.execute(query).fetchall()
    return result

# Функция для выбора всех записей из Employer по id регистрации
def select_employer_by_registration_id(registration_id):
    query = select(Employer).where(Employer.c.id == registration_id)
    result = conn.execute(query).fetchall()
    return result

# Вставка данных в Registration_data
insert_registration(13, datetime.now())

# Вставка данных в Applicant
aplicant_data = {
    'id': 1,  # Это id из Registration_data
    'fio': 'Иванов Иван',
    'exp': 5,
    'positions': 'Разработчик',
    'specialization': 'Python',
    'phone': '1234567890',
    'email': 'ivanov@example.com',
    'skills': 'Python, SQL',
    'relevance': True,
    'about': 'Опытный разработчик',
    'education': 'Высшее',
    'ready_trips': True,
    'age': 30,
    'registration': 'Москва',
    'type_employment': 'Полная занятость',
    'car': True,
    'drive_license': True,
    'languages': 'Русский, Английский',
    'salary': 100000,
    'city': 'Москва'
}
insert_aplicant(aplicant_data)

# Вставка данных в Employer
employer_data = {
    'id': 1,  # Это id из Registration_data
    'fio': 'Петров Петр',
    'vacancy': 'Разработчик',
    'phone': '0987654321',
    'email': 'petrov@example.com',
    'relevance': True,
    'requirements': 'Python',
    'requirement_age': 25,
    'requirement_registration': 'Москва',
    'type_employment': 'Полная занятость',
    'requirement_car': True,
    'requirement_drive_license': True,
    'salary': 120000,
    'city': 'Москва',
    'languages': 'Русский, Английский'
}
insert_employer(employer_data)

# Выбор всех записей из Registration_data
registrations = select_all_registration()
print(registrations)

# Выбор всех заявителей по id регистрации
applicants = select_aplicant_by_registration_id(1)
print(applicants)

# Выбор всех работодателей по id регистрации
employers = select_employer_by_registration_id(1)
print(employers)

# Удаление записи из Registration_data по id
delete_registration(1)
