from orm import Model, StringField, FloatField, IntegerField


class Todo(Model):
    __table__ = 'todo'

    id = IntegerField(primary_key=True)
    deadline = StringField(ddl='varchar(50)')
    title = StringField(ddl='varchar(50)')
    memo = StringField(ddl='varchar(50)')
