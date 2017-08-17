from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
from math import sin
source = ColumnDataSource(dict(x=[], y=[]))

fig = figure()
fig.line(x='x', y='y', source=source)

i = 0.0
def update():
    global i
    newdata = dict(x=[i], y=[sin(i)])
    source.stream(newdata, 100)
    i += 0.1

curdoc().add_root(fig)
curdoc().add_periodic_callback(update, 100)
