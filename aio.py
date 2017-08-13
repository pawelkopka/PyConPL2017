import asyncio
import time

from aiohttp import web

async def hello(req):
    return web.json_response('Hello PyCon!')


async def hello_wait(req):
    time.sleep(5)
    return web.json_response('Hello after sleep 5s')


async def hello_await(req):
    await asyncio.sleep(5)
    return web.json_response('Hello after asyncio sleep 5s')


app = web.Application()
app.router.add_get('/hello', hello)
app.router.add_get('/hello_wait', hello_wait)
app.router.add_get('/hello_await', hello_await)
web.run_app(app)

