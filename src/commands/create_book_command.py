from ..books_read.src.controllers import CreateBookController, \
    SearchTopicsController
from .command import Command


class CreateBookCommand(Command):

    def execute(self):
        topic_name = input('Ingrese nombre de tema')
        search_controller = SearchTopicsController()
        topics = search_controller.filter_by_name(topic_name)
        print('Temas disponibles')
        for i, topic in enumerate(topics):
            print('{0}) {1}'.format(i, topic.name))

        topic_selected = int(input('Seleccione el tema: '))
        topic = topics[topic_selected]
        title = input('Ingrese título: ')
        publication_date = input('Ingrese año de publicación: ')
        read_date = input('Ingrese fecha de lectura: ')
        create_controller = CreateBookController(
            title=title,
            publication_date=publication_date,
            read_date=read_date,
            topic=topic
        )
        create_controller.save()
        print('Libro registrado existosamente\n')
