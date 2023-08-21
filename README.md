# agenda_python

En la carpeta del proyecto crear un ambiente virtual por linea de comandos
python - n venv venv

Una vez creado el ambiente virtual ejecutar los comandos
cd venv\Scripts\
activate

Dentro de la carpeta del ambiente virtual 'venv' crear dos carpetas
datos
programas

Revisar las librerias que se tienen instalados con el comando
pip list

Debende salir las siguientes librearias
Package Version

---

autopep8 2.0.2
click 8.1.6
colorama 0.4.6
importlib-metadata 6.7.0
pip 23.2.1
pycodestyle 2.10.0
setuptools 40.8.0
tomli 2.0.1
typing_extensions 4.7.1
zipp 3.15.0

Si no salen entonces se deben de ejecutar los siguientes comandos
pip install click
pip install -U autopep8

Puede ser que el mismo paquete de pip este desactualizado
Esto se observa cuando se ejecuta
pip list

Si al final sale algo parecido a esto
You are using pip version 19.0.3, however version 23.2.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

Hay que ejecutar el comando mencionado
python -m pip install --upgrade pip
