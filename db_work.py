import sqlalchemy as db
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from datetime import datetime

engine = db.create_engine('sqlite:///myDatabase.db')
conn = engine.connect()
metadata = db.MetaData()

BASE_STRING_SIZE = 255
HASH_SIZE = 24

Registration_data = db.Table('Registration_data', metadata,
Column("id", Integer, primary_key=True),
Column("hash_key", String(HASH_SIZE)),
Column("data_reg", DateTime(), default=datetime.now))

Aplicant = db.Table('Aplicant', metadata,
Column("id", Integer, ForeignKey(Registration_data.c.id), primary_key=True),
Column("fio", String(BASE_STRING_SIZE)),
Column("exp", Integer),
Column("positions", Text),
Column("specialization", String(BASE_STRING_SIZE)),
Column("phone", String(BASE_STRING_SIZE)),
Column("email", String(BASE_STRING_SIZE)),
Column("skills", Text),
Column("relevance", Boolean),
Column("about", Text),
Column("education", Text),
Column("ready_trips", Boolean),
Column("age", Integer),
Column("registration", String(BASE_STRING_SIZE)),
Column("type_employment", String(BASE_STRING_SIZE)),
Column("car", Boolean),
Column("drive_license", Boolean),
Column("languages", Text),
Column("salary", Integer),
Column("city", String(BASE_STRING_SIZE)))

Employer = db.Table('Employer', metadata,
Column("id", Integer, ForeignKey(Registration_data.c.id), primary_key=True),
Column("fio", String(BASE_STRING_SIZE)),
Column("vacancy", String(BASE_STRING_SIZE)),
Column("phone", String(BASE_STRING_SIZE)),
Column("email", String(BASE_STRING_SIZE)),
Column("relevance", Boolean),
Column("requirements", Text),
Column("requirement_age", Integer),
Column("requirement_registration", String(BASE_STRING_SIZE)),
Column("type_employment", String(BASE_STRING_SIZE)),
Column("requirement_car", Boolean),
Column("requirement_drive_license", Boolean),
Column("salary", Integer),
Column("city", String(BASE_STRING_SIZE)),
Column("languages", Text))

metadata.create_all(engine)
