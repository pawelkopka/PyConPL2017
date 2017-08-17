from bokeh.plotting import figure, output_file, show

x = range(10)
y = [i**2 for i in x]

output_file("kreska.html")

p = figure(title="Pierwsza kreska", x_axis_label='x', y_axis_label='x**2')

p.line(x, y, legend="x do kwadratu", line_width=2)

show(p)