import logging; logging.basicConfig(level=logging.INFO)
import asyncio, json
from aiohttp import web

# import config file
from config import configs

import orm
from coroweb import add_routes


# URL log factory
async def logger_factory(app, handler):
    async def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        return (await handler(request))
    return logger


# data factory
async def data_factory(app, handler):
    async def parse_data(request):
        if request.method == 'POST':
            if request.content_type.startswith('application/json'):
                request.__data__ = await request.json()
                logging.info('request json: %s' % str(request.__data__))
        return (await handler(request))
    return parse_data


# response factory
async def response_factory(app, handler):
    async def response(request):
        logging.info('Response handler...')
        r = await handler(request)
        if isinstance(r, dict):
            resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
            resp.content_type = 'application/json;charset=utf-8'
            return resp
        elif isinstance(r, list):
            if len(r) == 3:
                resp = web.HTTPNotFound(body="{'status':%s, 'message':%s, 'id':%s}" % (r[0], r[1], r[2]))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            elif len(r) == 2:
                resp = web.HTTPNotFound(body="{'status':%s, 'message':%s}" % (r[0], r[1]))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
        else:
            resp = web.HTTPBadRequest(body="{'status':'failure', 'message':'Invalid request'}")
            resp.content_type = 'application/json;charset=utf-8'
            return resp
    return response


async def init(loop):
    await orm.create_pool(loop=loop, **configs.db)
    app = web.Application(loop=loop, middlewares=[
        logger_factory, response_factory
    ])
    add_routes(app, 'handlers')
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8080)
    logging.info('server started at http://127.0.0.1:8080...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
