¿Cuáles son los diferentes tipos de bucles en Python? 
=====================================================

Los bucles en Python sirven para automatizar la ejecución del código, que en este lenguaje se realiza de forma secuencial, es decir sigue un orden lineal. 
Existen dos tipos: bucle for y bucle while. 

Bucle for
---------
Un bucle for se utiliza para iterar sobre una secuencia, es decir, sobre una lista, una tupla, un diccionario, un conjunto o una cadena.
La iteración depende de la cantidad de objetos recogidos en las líneas y finalizará cuando se completen todos los valores de la lista.  

.. admonition:: Nota

    El bucle for no requiere que se establezca una variable de indexación de antemano.

Ejemplo

Imprime los elementos de un lista:

.. code-block:: python

    lenguajes = ["Python", "C", "C++", "Java"]
    for lenguaje in lenguajes:
        print(lenguaje)

Ejemplo

Imprime números del 1 al 10

.. code-block:: python

    for contador in range(1, 11):
        print(contador)

.. admonition:: Nota

    Cuidado al utilizar range si quiero mostrar números del 1 al 10, el segundo parámetro corresponde a la posición que quieres que pare (y no lo incluye).
    Por eso que en el ejemplo se utilice range(1,11)

Bucle while
-----------
El bucle while se suele utilizar cuando no se conoce el número exacto de repeticiones que se darán en el código.  
La palabra reservada "while" ejecuta una porción de código una y otra vez hasta que la condición especificada sea falsa. Es decir, ejecuta una porción de código mientras que la condición sea verdadera.

Ejemplo

Imprime ¡Hola, mundo! siempre que sea menor que 10:

.. code-block:: python

    contador = 1
    while contador < 10:
        print("¡Hola, mundo!")
        contador += 1

.. admonition:: Nota
    
    El bucle while requiere que se establezca una variable de indexación de antemano.

    .. code-block:: python

        contador = 1
        while contador < 10:
            print("¡Hola, mundo!")
      
    Si no incrementamos el ``contador``, el while anterior entrará en lo que se conoce como bucle infinito.

Control de los bucles
---------------------

Break
~~~~~

La expresión ``break`` se utiliza para romper el código, es decir, mientras que continue impide que el bucle de Python de paso a la progresión secuencial y, por lo tanto, pare antes de tiempo la iteración del bloque.  

Ejemplo while

Sale del bucle cuando el contador es 4 con lo que imprimirá por pantalla ¡Hola, mundo! solo 4 veces

.. code-block:: python

    contador = 1
    while contador < 10:
        print(contador)
        if contador == 4:
            break
        contador += 1

Ejemplo loop

Sale del bucle cuando el lenguaje es C++ con lo que imprimirá solo estos tres lenguajes "Python", "C" y "C++"

.. code-block:: python

    lenguajes = ["Python", "C", "C++", "Java"]
    for lenguaje in lenguajes:
        print(lenguaje)
        if x == "C++":
            break
 

Continue
~~~~~~~~
Con la instrucción ``continue`` podemos detener la iteración actual y continuar con la siguiente.

Ejemplo while

Si contador es igual a 4 continue con la siguiente iteración y no imprima el numero 4

.. code-block:: python

    contador = 1
    while contador < 10:
        if contador == 4:
            break
        print(contador)
        contador += 1

Ejemplo loop

No imprimirá el lenguaje "C++"

.. code-block:: python

    lenguajes = ["Python", "C", "C++", "Java"]
    for lenguaje in lenguajes:
        if x == "C++":
            continue
        print(lenguaje)

Bucles anidados
---------------
En Python pueden programarse bucles aislados o estos loops pueden formar parte de sentencias de otros bloques, convirtiéndose en bucles anidados.
Se habla de bucles anidados cuando un bucle se encuentra en el bloque de instrucciones de otro bloque.
Al bucle que se encuentra dentro del otro se le puede denominar bucle interior o bucle interno. 
El otro bucle sería el bucle exterior o bucle externo.

Los bucles pueden tener cualquier nivel de anidamiento (un bucle dentro de otro bucle dentro de un tercero, etc.).
Aunque en Python no es necesario, se recomienda que los nombres de las variables de control de los bucles anidados no coincidan, para evitar ambigüedades.

Bucle anidado con variables independientes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando los valores que toma la variable de control del bucle interno no dependen del valor de la variable de control del bucle externo.

Ejemplo bucle anidado variables independiente

.. code-block:: python

    for i in [0, 1, 2]:
        for j in [0, 1]:
            print(f"i vale {i} y j vale {j}")

Bucle anidado con variables dependientes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando los valores que toma la variable de control del bucle interno dependen del valor de la variable de control del bucle externo

Ejemplo bucle anidado variables dependiente

.. code-block:: python

    for i in [1, 2, 3]:
        for j in range(i):
            print(f"i vale {i} y j vale {j}")

¿Por qué son útiles?
--------------------
Los bucles son una herramienta para alterar el flujo normal de un programa. 
Nos permiten repetir una porción de código tantas veces como queramos.

Resources
---------
* `Python Bucle For <https://www.w3schools.com/python/python_for_loops.asp>`_
* `Python Bucle While <https://www.w3schools.com/python/python_while_loops.asp>`_
* `Bucles <https://tutorial.recursospython.com/bucles/#bucles>`_
* `Función Range <https://www.w3schools.com/python/ref_func_range.asp>`_


