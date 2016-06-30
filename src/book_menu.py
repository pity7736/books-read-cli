from src.books_read.src.controllers import CreateBookController, \
    SearchTopicsController

from .menu import Menu


class BookMenu(Menu):
    name = 'Menú de libros'
    options = '''
    0) Menú principal
    1) Registrar
    '''

    def __init__(self):
        super(BookMenu, self).__init__()
        self.data = {}

    def _run_selected_option(self):
        if not self._selected_option:
            self._set_option()

        if self._selected_option == '0':
            print('Saliendo al menú principal...\n')
            return
        elif self._selected_option == '1':
            self._ask_data()
            create_controller = CreateBookController(**self.data)
            create_controller.save()
            print('Libro creado exitosamente')

        self.run()

    def _ask_data(self):
        title = input('Ingrese título: ')
        publication_date = input('Ingrese año de publicación: ')
        read_date = input('Ingrese fecha de lectura: ')
        self.data['title'] = title
        self.data['publication_date'] = publication_date
        self.data['read_date'] = read_date
        self._ask_topic()

    def _ask_topic(self):
        topic_name = input('Ingrese nombre de tema: ')
        search_controller = SearchTopicsController()
        topics = search_controller.filter_by_name(topic_name)
        print(dir(topics))
        print('Listado de temas disponibles:')
        for i, topic in enumerate(topics):
            print('{0}) {1}'.format(i, topic.name))

        topic_selected = int(input('Seleccione el tema: '))
        topic = topics[topic_selected]
        self.data['topic'] = topic
