import asyncio
import json

from aiohttp import ClientSession
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import Figure

i = 1
loop = asyncio.get_event_loop()
url = 'http://127.0.0.1:8080/{}'

fig = Figure()
source = ColumnDataSource(dict(x=[], y=[]))
fig.line(x='x', y='y', source=source)

async def fetch_data(data):
    async with ClientSession() as session:
        url_data = url.format(data)
        async with session.get(url_data) as resp:
            data = json.loads(await resp.text())
            return data['data']

def update():
    global i
    data = loop.run_until_complete(fetch_data('cpu_percent'))
    newdata = dict(x=[i], y=[data])
    source.stream(newdata, 100)
    i += 1

curdoc().add_root(fig)
curdoc().add_periodic_callback(update, 100)



