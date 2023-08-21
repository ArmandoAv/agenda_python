"""
    Programa que utiliza la linea de comandos para crear una agenda
    La agenda se guarda en un archivo de tipo json
    Con los siguientes datos
    ID del usuario
    Nombre del usuario
    Apellido del usuario
    Numero de celular del usuario
	El programa tiene las siguientes funciones
	Agrega un usuario a la bitacora
	Actualiza los datos de un usuario
	Busca un usuario en especifico
	Despliega a todos los usuarios
"""
import manipula_bitacora
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--nombre', required=True, help='Nombre del usuario')
@click.option('--apellido', required=True, help='Apellido del usuario')
@click.option('--numero_celular', required=True, help='Numero de celular de un usuario sin guiones, espacios ni letras')
@click.pass_context
# Crea un nuevo usuario en la bitacora
def nuevo_usuario(ctx, nombre, apellido, numero_celular):
    if not nombre or not apellido or not numero_celular:
        ctx.fail('El nombre, el apellido y el numero de celular son requeridos')
    else:
        """
            Obtenemos el maximo id del archivo
            Se puede hacer con len() pero si por algun motivo
            Se borro un id que no es el maximo se pueden repetir los ids
        """
        datos = manipula_bitacora.leer_json()
        ult_usuario = str(datos[-1])
        ult_id = ult_usuario[:ult_usuario.find(',')]
        nuevo_id = int(ult_id[ult_id.find(':') + 1:]) + 1
        nuevo_usuario = {
            'id': nuevo_id,
            'nombre': nombre,
            'apellido': apellido,
            'numero_celular': int(numero_celular)
        }
        datos.append(nuevo_usuario)
        manipula_bitacora.escribir_json(datos)
        print(f"El usuario {nombre} {apellido} ha sido creado satisfactoriamente con el id: {nuevo_id}."
              "\nPara consultarlo revise en la bitacora con el comando usuarios.")


@cli.command()
@click.argument('id', type=int)
# Busca un usuario en la bitacora
def busca_usuario(id):
    datos = manipula_bitacora.leer_json()
    usuario = next((x for x in datos if x['id'] == id), None)
    if usuario is None:
        print(f"El usuario con el id {id} no se encuentra")
    else:
        print(
            f"{usuario['id']} - {usuario['nombre']} - {usuario['apellido']} - {usuario['numero_celular']}")


@cli.command()
@click.argument('id', type=int)
@click.option('--nombre', help='Nombre de un usuario')
@click.option('--apellido', help='Apellido de un usuario')
@click.option('--numero_celular', help='Numero de celular de un usuario sin guiones, espacios ni letras')
# Actualiza un usuario en la bitacora
def actualiza_usuario(id, nombre, apellido, numero_celular):
    datos = manipula_bitacora.leer_json()
    for usuario in datos:
        if usuario['id'] == id:
            if nombre is not None:
                usuario['nombre'] = nombre
            if apellido is not None:
                usuario['apellido'] = apellido
            if numero_celular is not None:
                usuario['numero_celular'] = int(numero_celular)
            break
    manipula_bitacora.escribir_json(datos)
    print(f"El susario con id {id} ha sido actualizado"
          "\nFavor de validar los cambios en la bitacora con el comando usuarios.")


@cli.command()
@click.argument('id', type=int)
# Borra un usuario de la bitacora
def borra_usuario(id):
    datos = manipula_bitacora.leer_json()
    usuario = next((x for x in datos if x['id'] == id), None)
    if usuario is None:
        print(f"El usuario con el id {id} no se encuentra")
    else:
        datos.remove(usuario)
        manipula_bitacora.escribir_json(datos)
        print(f"El usuario con el id {id} fue borrado satisfactoriamente."
              "\nPara consultar que ya no existe revise la bitacora con el comando usuarios.")


@cli.command()
# Lista los usuarios de la bitacora
def usuarios():
    datos = manipula_bitacora.leer_json()
    for usuario in datos:
        print(
            f"{usuario['id']} - {usuario['nombre']} - {usuario['apellido']} - {usuario['numero_celular']}")


if __name__ == '__main__':
    cli()
