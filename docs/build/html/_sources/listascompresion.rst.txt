¿Qué es una lista por comprensión en Python?
============================================

Las comprensiones de listas proporcionan una forma corta y concisa de crear listas ahorrandonos escribir muchas líneas de código.
Se usan con corchetes [] y en su interior contienen una expresión seguida de un bucle for y cero o más sentencias for o if. 
La expresión puede ser cualquier cosa que se te ocurra, lo que significa que puedes usar cualquier tipo de objetos en la lista. 
El resultado es una nueva lista creada tras evaluar las expresiones que haya dentro.

Ejemplo método tradicional

Imprimir los números del 0 al 29 divisibles por 3

.. code-block:: python

    multiples = []
    for i in range(30):
        if i % 3 == 0:
            multiples.append(i)
        print(multiples)
     # Salida: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

Ejemplo con una lista por compresión

Imprimir los números del 0 al 29 divisibles por 3

.. code-block:: python

    multiples = [i for i in range(30) if i % 3 == 0]
    print(multiples)
    # Salida: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]


Resources
---------
* `Python Listas de Compresión <https://www.learnpython.org/es/List%20Comprehensionsp>`_
* `Compresión de listas Python <https://docs.hektorprofe.net/python/funcionalidades-avanzadas/comprension-de-listas/>`_
* `El libro de Python <https://ellibrodepython.com/list-comprehension-python>`_