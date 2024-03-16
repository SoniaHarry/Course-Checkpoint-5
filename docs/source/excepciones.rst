Python - Control de Errores
===========================

Cuando ocurre un error, o una excepción, Python normalmente se detendrá y generará un mensaje de error.

Try
---
Para evitar que el programa se detenga existen las excepciones, que se manejan usando la declaración ``try:```

Ejemplo

El bloque try generará una excepción porque x no esta definida y mostrará un mensaje

.. code-block:: python

    try:
        print(x)
    except:
        print("Ha ocurrido un error")

Except
------
El bloque except te permite manejar el error.

Ejemplo

.. code-block:: python

    try:
        print(x)
    except:
        print("Ha ocurrido un error")

Else
----
El bloque else te permite ejecutar código cuando no hay ningún error.

Ejemplo

.. code-block:: python

    try:
        print("Hola")
    except:
        print("Ha ocurrido un error")
    else:
        print("Todo ha ido bien")


Finally
-------
El bloque ``finally``, si se especifica, se ejecutará independientemente de si el bloque try genera un error o no.

Ejemplo

.. code-block:: python

    try:
        print(x)
    except:
        print("Ocurrio un error")
    finally:
        print("The 'try except' is finished")

Resources
---------
* `Python Control de Excepciones <https://www.w3schools.com/python/python_try_except.asp>`_
