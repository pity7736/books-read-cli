from src.books_read.src.controllers import CreateTopicController

from .menu import Menu
from src.books_read.src.controllers.search_topics import SearchTopicsController


class TopicMenu(Menu):
    name = 'Menú de Temas'
    options = '''
    0) Menú principal
    1) Registrar
    2) Buscar por nombre
    3) Listar todos los temas
    '''

    def __init__(self):
        super(TopicMenu, self).__init__()
        self.name_topic = None
        self.topics = ()

    def _run_selected_option(self):
        if not self._selected_option:
            self._set_option()

        if self._selected_option == '0':
            print('Saliendo al menú principal...\n')
            return
        elif self._selected_option == '1':
            self._ask_name()
            create_controller = CreateTopicController(self.name_topic)
            create_controller.save()
            print('Tema registrado exitosamente.\n')
        elif self._selected_option == '2':
            self._ask_name()
            search_controller = SearchTopicsController()
            self.topics = search_controller.filter_by_name(self.name_topic)
            self._print_result()
        elif self._selected_option == '3':
            search_controller = SearchTopicsController()
            self.topics = search_controller.get_all()
            self._print_result()

        print()
        self.run()

    def _ask_name(self):
        self.name_topic = input('ingrese nombre tema: ')

    def _print_result(self):
        print('Listado de temas:')
        for topic in self.topics:
            print(topic.name)
