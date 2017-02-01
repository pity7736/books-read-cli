from .command import Command
from ..books_read.src.controllers.create_topic import CreateTopicController


class CreateTopicCommand(Command):

    def execute(self):
        name_topic = input('ingrese nombre de tema: ')
        create_controller = CreateTopicController(name_topic)
        create_controller.save()
        print('Tema registrado existosamente\n')
