from ..books_read.src.controllers import CreateAuthorController
from .command import Command


class CreateAuthorCommand(Command):

    def execute(self):
        first_name = input('Ingrese nombre: ')
        last_name = input('Ingrese apellido: ')
        create_controller = CreateAuthorController(
            first_name=first_name,
            last_name=last_name
        )
        create_controller.save()
        print('Autor registrado exitosamente\n')
