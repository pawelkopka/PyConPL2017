Bokeh
=======================================================================================
.. image:: pycon2017.png
   :width: 100px
   :height: 100px
   :scale: 100 %
   :alt: alternate text
   :align: right

Interaktywna biblioteka do wizualizacji za pośrednictwem przeglądarek internetowych w stylu D3.js

Alternatywy
******************

- Matplotlib + mpld3
- Plotly
- i wiele innych `Awesome data visualization tools in Python <https://www.youtube.com/watch?v=OC-YdBz8Llw&t=/>`_


Pierwsze kreski
-------------------

.. literalinclude:: przyklad_bokeh.py
   :lines: 1-12

.. raw:: html
   :file: kreska.html

Pierwszy stream
-------------------

.. literalinclude:: przyklad_bokeh2.py
   :lines: 1-17

.. testoutput::

   $ bokeh serve --show przyklad_bokeh2.py
   2017-08-17 10:25:52,014 Starting Bokeh server version 0.12.6 (running on Tornado 4.4.2)
   2017-08-17 10:25:52,018 Starting Bokeh server on port 5006 with applications at paths ['/przyklad_bokeh2']
   2017-08-17 10:25:52,019 Starting Bokeh server with process id: 21773
   2017-08-17 10:25:52,266 200 GET /przyklad_bokeh2 (127.0.0.1) 146.18ms
   2017-08-17 10:25:52,672 WebSocket connection opened
   2017-08-17 10:25:52,672 ServerConnection created