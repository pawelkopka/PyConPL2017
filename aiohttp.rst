Aiohttp
=======================================================================================
.. image:: pycon2017.png
   :width: 100px
   :height: 100px
   :scale: 100 %
   :alt: alternate text
   :align: right

Aiohttp
********

Asynchroniczny klient/serwer HTTP.

Mikro framework jak Flask

Pierwsza aplikacja
*********************
.. literalinclude:: aio.py
   :lines: 3-7, 19-21, 24

.. testoutput::

   $ curl localhost:8080/hello
   "Hello PyCon!"

Poczekajmy chwilę(asyncio)
**************************
.. literalinclude:: aio.py
   :lines: 1, 14-17

.. testoutput::

   $ time curl localhost:8080/hello_await
   "Hello after asyncio sleep 5s"
   real    0m5.019s
   user    0m0.012s
   sys     0m0.000s


Poczekajmy chwilę(time)
************************
.. literalinclude:: aio.py
   :lines: 2, 9-12

.. testoutput::

   $ time curl localhost:8080/hello_wait
   "Hello after sleep 5s"
   real    0m5.012s
   user    0m0.006s
   sys     0m0.000s

Minus asyncio
*************************
.. testoutput::

   $ time curl localhost:8080/hello          │$ time curl localhost:8080/hello_await
   "Hello PyCon!"                            │"Hello after asyncio sleep 5s"
   real    0m0.016s                          │real    0m5.021s
   user    0m0.001s                          │user    0m0.011s
   sys     0m0.011s                          │sys     0m0.007s
   $                                         │
   $ time curl localhost:8080/hello          │$ time curl localhost:8080/hello_wait
   "Hello PyCon!"                            │"Hello after sleep 5s"
   real    0m5.216s                          │real    0m5.045s
   user    0m0.001s                          │user    0m0.011s
   sys     0m0.011s                          │sys     0m0.007s



:Linki:     #TODO zmień linki
    `aiohttp <https://docs.python.org/3/library/asyncio-task.html>`_

