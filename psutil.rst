Psutil
=======================================================================================
.. image:: pycon2017.png
   :width: 100px
   :height: 100px
   :scale: 100 %
   :alt: alternate text
   :align: right

Między systemowa bibliotek dostarczające informacje o zużyciu systemu operacyjnego oraz działających na nim procesach.

Początki z psutil
******************

Ile mam procesorów?
-------------------
.. literalinclude:: przyklad_psutil.py
   :lines: 1-4

.. testoutput::

   $ python3.6 cpu_psutil.py
   mam całe 4 procesory

Jakie jest zużycie procesora?
-----------------------------
.. literalinclude:: przyklad_psutil.py
   :lines: 6-7

.. testoutput::

   $ python3.6 cpu_percent_psutil.py
   właśnie zużywam  3.7% procesorów



Co z moją pamięcią?
-----------------------------
.. literalinclude:: przyklad_psutil.py
   :lines: 9-10

.. testoutput::

   $ python3.6 memory_psutil.py
   pamięć wirtualna svmem(total=16744116224, available=12605980672, percent=24.7, used=3568963584, free=11050737664, active=4058066944, inactive=1285193728, buffers=153546752, cached=1970868224, shared=348962816)


Ile zjada lis?
----------------------------
.. literalinclude:: przyklad_psutil.py
   :lines: 12-21

.. testoutput::

   $ python3.6 lisek_psutil.py
   psutil.Process(pid=5052, name='firefox')
   lis zjada 35.5%
   io lisa pio(read_count=2242044, write_count=2206770, read_bytes=175054848, write_bytes=2857779200, read_chars=8978109464, write_chars=3143650749)


Może też zarządzać procesami
------------------------------

.. literalinclude:: przyklad_psutil.py
   :lines: 23-29

.. testoutput::

   $ python3.6 przyklad_psutil.py
   psutil.Process(pid=882, name='python3.6')
   Killed

:Linki:
   `psutil-doc <https://pythonhosted.org/psutil/>`_
