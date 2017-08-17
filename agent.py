import psutil
from aiohttp import web


async def cpu_percent(request):
    query = request.rel_url.query
    return web.json_response(dict(data=psutil.cpu_percent(interval=float(query.get('interval', 0)),
                                                          percpu=bool(query.get('percpu', False)))),
                             status=200)

async def virtual_memory(request):
    return web.json_response(dict(data=psutil.virtual_memory()))


async def cpu_times_percent(request):
    query = request.rel_url.query
    return web.json_response(dict(data=psutil.cpu_times_percent(percpu=bool(query.get('percpu', False)))),
                             status=200)

app = web.Application()
app.router.add_get('/cpu_percent', cpu_percent)
app.router.add_get('/virtual_memory', virtual_memory)
app.router.add_get('/cpu_times_percent', cpu_times_percent)
web.run_app(app)