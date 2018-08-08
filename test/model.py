from peewee import *;

db = SqliteDatabase('people.db');

# Model
class Person(Model):
    name = CharField();
    birthday = DateField();

    class Meta:
        database = db;

# Create Tables
db.connect();
db.create_tables([Person]);

# Storing data
from datetime import date
uncle_bob = Person(name = 'Bob', birthday = date(1960, 1, 15));
uncle_bob.save();
