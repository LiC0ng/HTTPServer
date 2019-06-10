from models import Todo
from coroweb import get, post, delete
import re


@get('/api/v1/todo')
async def fetchAll(request):
    todo = await Todo.findAll()
    return {'events': todo}


@get('/api/v1/todo/{id}')
async def fetchOne(id):
    todo = await Todo.find(id)
    if todo is None:
        result = ['failure', 'Event not found', id]
        return result
    return todo

_RE_RFC3339 = re.compile(r'^([0-9]+)-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]+)?(([Zz])|([\+|\-]([01][0-9]|2[0-3]):[0-5][0-9]))$')


@post('/api/v1/todo')
async def register(*, deadline, title, memo):
    if not _RE_RFC3339.match(deadline):
        result = ['failure', 'Invalid data format']
        return result

    nextid = await Todo.nextId()
    if not nextid["Max(id)"]:
        nextid["Max(id)"] = 0
    id = nextid["Max(id)"] + 1
    todo = Todo(id=id,
                deadline=deadline,
                title=title,
                memo=memo)
    await todo.save()
    result = {'status': 'success', 'message': 'registered', 'id': id}
    return result


@delete('/api/v1/todo/{id}')
async def deleteEvent(id):
    todo = await Todo.find(id)
    if todo is None:
        result = ['failure', 'Event not found', id]
        return result
    await todo.remove()
    result = {'status': 'success', 'message': 'deleted', 'id': id}
    return result
