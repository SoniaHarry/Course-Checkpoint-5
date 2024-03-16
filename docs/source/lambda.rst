¿Qué es una función Lambda en Python?
=====================================

Las funciones lambda en Python son un tipo de funciones que se definen en una línea y cuyo código a ejecutar suele ser pequeño. 
El término “función lambda” significa función anónima en Python. 
Para crear una función lambda, Python utiliza la palabra clave lambda. 
Una expresión lambda consiste en la palabra clave lambda seguida de una lista de argumentos, dos puntos y una única expresión (“expression”). 

lambda argument: expression

En cuanto se llama la función lambda, se proporciona la expresión con los argumentos y se evalúa.

A continuación mostramos las dos formas de hacerlo; utilizando una función normal y utilizando lambda. 

.. code-block:: python

    # Función normal
    def squared (num): 
        return (num * num)


    # print 81
    print (squared(9))

.. code-block:: python

    # Función lambda
    squared = lambda num: num * num


    # print 81
    print (squared(9))

.. admonition:: Nota

    En Python, el término “función lambda”se refiere a una función creada con la palabra clave lambda. 
    Lambda no es el nombre de una función y tampoco es uno de los operadores de Python.

Resources
---------
* `Python función lambda <https://ellibrodepython.com/lambda-python>`_