from peewee import *

db = SqliteDatabase('deba.db')


class Card(Model):
    rank = CharField()
    suit = CharField()
    value = IntegerField()

    class Meta:
        database = db  # This model uses the "people.db" database.


if __name__ == '__main__':
    db.connect()
    db.create_tables([Card], safe=True)
