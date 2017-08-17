Prosty Monitoring
=======================================================================================
.. image:: pycon2017.png
   :width: 100px
   :height: 100px
   :scale: 100 %
   :alt: alternate text
   :align: right


Agent
******
.. literalinclude:: agent.py
   :lines: 1-25

.. testoutput::

   $ python3.6 agent.py
   ======== Running on http://0.0.0.0 ========
   (Press CTRL+C to quit)

Monitoring
***********
.. literalinclude:: monitoring.py
   :lines: 1-32

.. testoutput::

   $ bokeh serve --show monitoring.py
   2017-08-17 12:17:07,244 Starting Bokeh server version 0.12.6 (running on Tornado 4.4.2)
   2017-08-17 12:17:07,247 Starting Bokeh server on port 5006 with applications at paths ['/monitoring']
   2017-08-17 12:17:07,247 Starting Bokeh server with process id: 28258
   2017-08-17 12:17:07,531 200 GET /monitoring (127.0.0.1) 184.44ms
   2017-08-17 12:17:07,959 WebSocket connection opened
   2017-08-17 12:17:07,959 ServerConnection created

