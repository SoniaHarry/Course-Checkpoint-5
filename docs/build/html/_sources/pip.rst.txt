¿Qué es un paquete pip?
=======================

La aplicación pip es la herramienta fundamental que trae Python para la instalación de paquetes para poder utilizarlos en nuestros proyectos.
Se utiliza para instalar, desinstalar y actualizar paquetes de Python.

PyPI: Gestión de Paquetes en Python con pip y PyPI
En Python, los paquetes son una forma de organizar el código en unidades reutilizables. 
Un paquete puede contener módulos, clases, funciones, variables y otros recursos.

PyPI es un repositorio de paquetes de Python. 
Es una forma de compartir y encontrar paquetes de Python creados por otros desarrolladores.

Instalar PyPI y pip
-------------------

PyPI y pip están incluidos en la instalación predeterminada de Python. Si no tienes Python instalado, puedes descargarlo desde el sitio web de Python.

Para verificar que tienes PyPI y pip instalados, abre una terminal y ejecuta los siguientes comandos:

.. code-block:: console

    python -m pip --version

Si tienes PyPI y pip instalados, verás una salida similar a la siguiente:

.. code-block:: console

    pip 22.0.4 from /usr/local/lib/python3.11/site-packages/pip (python 3.11)

Instalar un paquete de PyPI
---------------------------

Para instalar un paquete de PyPI, utiliza el comando pip install. El siguiente comando instala el paquete numpy:

.. code-block:: console

    pip install numpy


Desinstalar un paquete de PyPI
------------------------------

Para desinstalar un paquete, utiliza el comando pip uninstall:

.. code-block:: console

    pip uninstall numpy

Resources
---------
* `Python Gestión de paquetes <https://codigospython.com/pypi-gestion-de-paquetes-en-python-con-pip-y-pypi/>`_
* `Python Pip <https://www.w3schools.com/python/python_pip.asp>` _