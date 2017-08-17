Asynchroniczność
=======================================================================================
.. image:: pycon2017.png
   :width: 100px
   :height: 100px
   :scale: 100 %
   :alt: alternate text
   :align: right

Korutyny
*********

- korutyny vs generatory

- korutyna -> korutyna -> korytuna -> korytuna -> rutyna -> rutyna

python3.4 ::

    import asyncio

    @asyncio.coroutine
    def hello():
        print('hello')
        yield from asyncio.sleep(1.0)
        print('for other side')

python3.5+ ::

    import asyncio

    async def hello():
        print('hello')
        await asyncio.sleep(1.0)
        print('for other side')

Pętla zdarzeń
**************
- jeden wątek
- jeden proces
- zarządca zadań


Przykład z życia
*****************

Synchroniczny poranek

.. literalinclude:: przyklad_sync.py
   :lines: 1-43

.. testoutput::

   $ python3.6 przyklad_sync.py
   włącz czajnik
   zaparz herbatę
   wypij herbatę
   prysznic zajęty
   prysznic zajęty
   prysznic zajęty
   weź prysznic
   zr»b kanapki
   spakować do plecaka ['kanapki']
   Czas : 9.009146451950073

Asynchroniczny poranek

.. literalinclude:: przyklad_async.py
   :lines: 1-45

.. testoutput::

   $ python3.6 przyklad_async.py
   zrób kanapki
   włącz czajnik
   prysznic zajęty
   prysznic zajęty
   spakować do plecaka ['kanapki']
   zaparz herbatę
   prysznic zajęty
   weź prysznic
   wypij herbatę
   Czas : 4.002426624298096



:Linki:
    `asyncio-task <https://docs.python.org/3/library/asyncio-task.html>`_

    `PEP 3156 <https://www.python.org/dev/peps/pep-3156/>`_

