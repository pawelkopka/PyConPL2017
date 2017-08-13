Asynchroniczność
=======================================================================================
.. image:: pycon2017.png
   :width: 400px
   :height: 200px
   :scale: 50 %
   :alt: alternate text
   :align: right

Korutyny
*********

- korutyny vs generatry

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

#TODO  dodaj rysunek petli zdarzen

Przykład z życia
*****************

Synchroniczny poranek

.. literalinclude:: przyklad_sync.py
   :lines: 1-43

.. testoutput::

   $ python3.6 przyklad_sync.py
   włącz czajknik
   zaparz hebatę
   wypij herbate
   prysznic zajety
   prysznic zajety
   prysznic zajety
   weź prysznic
   zrob kanapki
   spkować do plecaka ['kanapki']
   Czas : 9.009146451950073

Asynchroniczny poranek

.. literalinclude:: przyklad_async.py
   :lines: 1-45

.. testoutput::

   $ python3.6 przyklad_async.py
   zrob kanapki
   włącz czajknik
   prysznic zajety
   prysznic zajety
   spkować do plecaka ['kanapki']
   zaparz hebatę
   prysznic zajety
   weź prysznic
   wypij herbate
   Czas : 4.002426624298096

:Linki:
    `asyncio-task <https://docs.python.org/3/library/asyncio-task.html>`_

    `PEP 3156 <https://www.python.org/dev/peps/pep-3156/>`_

