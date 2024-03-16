¿Qué es un condicional?
=======================

Python admite los siguientes condicionales:

* Es igual a: a == b
* No es igual a: a != b
* Menos que: a < b
* Menor o igual a: a <= b
* Mayor que: a > b
* Mayor o igual a: a >= b

Los condicionales se utilizan de varias maneras, las más usadas en "sentencias if" y "bucles".

Una "sentencia if" permite la ejecución condicional de fragmentos de código. 
Un condicional expresa una acción que se realizará si se cumple una condición. 

.. admonition:: Nota

   Python se basa en la ``sangría`` (espacios en blanco al principio de una línea) para definir el alcance en el código

Si la ``sangria`` no es correcta se generará un error como vemos a continuación:

.. code-block:: python
     
    if edad >=18:
    print ('Puedes ir a la discoteca')

.. error:: Error 
    IndentationError: expected an indented block after 'if' statement on line 1

If
---

Una "sentencia if" se escribe utilizando la palabra clave "**if**". 

Ejemplo

Si nuestros hijos son mayores de edad podrán ir a la discoteca. 
La condición es que su edad sea mayor ó igual a 18 y la acción es que si se cumple la condición, podrá ir a la discoteca.

.. code-block:: python

    if edad >=18:
        print ('Puedes ir a la discoteca')


Elif
----

La palabra clave "**elif**" es la forma que tiene Python de decir "si las condiciones anteriores no son verdaderas, intente esta condición".

Ejemplo

Si queremos comparar dos números.
La primera condición comprueba si "a" es mayor que "b", si no lo es entonces comprueba si "a" y "b" son iguales.

.. code-block:: python

    a=3
    b=3
    if a > b:
        print ('a es mayor que b')   
    elif a==b:
        print ('Los números son iguales')   

Else
----

La palabra clave "**else**" captura cualquier cosa que no esté cubierta por las condiciones anteriores.

Ejemplo

Siguiendo con el ejemplo anterior si queremos comparar dos números. 
La primera condición comprueba si "a" es mayor que "b", si no lo es entonces comprueba si "a" y "b" son iguales, si esta tampoco se cumple entoces entra por el else y muestra que "a es menor que b". 

.. code-block:: python

    a=2
    b=3
    if a > b:
        print ('a es mayor que b')
    elif a==b:
        print ('a y b son iguales')
    else:
        print ('a es menor que b')

También puedes tener un else sin elif

.. code-block:: python

    a=2
    b=3
    if a > b:
        print ('a es mayor que b')
    else:
        print ('a no es mayor que b')

Short Hand If
-------------

Si solo tiene una declaración para ejecutar, puede colocarla en la misma línea que la "declaración if":

.. code-block:: python

    if a > b: print("a es mayor que b")

Short Hand If...Else
--------------------

Si solo tiene una declaración para ejecutar, una para "if" y otra para "else", puede ponerlas todas en la misma línea:

.. code-block:: python

    a=5
    b=3
    print("A") if a > b else print("B")

Operadores Ternarios 
--------------------

También puedes tener varias declaraciones "else" en la misma línea.
Esta técnica se conoce como "Operadores Ternarios" ó "Expresiones Condicionales".

.. code-block:: python

    a = 5
    b = 5
    print("A") if a > b else print("=") if a == b else print("B")   

And
---

La palabra clave "**and**" es un operador lógico y se utiliza para combinar declaraciones condicionales.

.. code-block:: python

    a = 200
    b = 33
    c = 500
    if a > b and c > a:
        print("Ambas condiciones son verdaderas")

Or
---

La palabra clave "**or**" es un operador lógico y se utiliza para combinar declaraciones condicionales.

.. code-block:: python

    a = 200
    b = 33
    c = 500
    if a > b or a > c:
        print("Por lo menos una de las condiciones es verdadera")

Not
---

La palabra clave "**not**" es un operador lógico y se utiliza para invertir el resultado de la declaración condicional.

.. code-block:: python

    a = 33
    b = 200
    if not a > b:
        print("a no es mayor que b")

Nested If
---------

Puede tener sentencias "if" dentro de declaraciones "if", esto se llama sentencias "if anidadas".

.. code-block:: python

    x = 41

    if x > 10:
        print("Above ten,")
        if x > 20:
            print("and also above 20!")
        else:
            print("but not above 20.")

Resources
---------
* `Python Conditions and If statements <https://www.w3schools.com/python/python_conditions.asp>`_
* `Python Control de flujo - Condicionales  <https://tutorial.recursospython.com/control-de-flujo/#condicional>`_
