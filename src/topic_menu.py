from src.books_read.src.controllers import CreateTopicController

from .menu import Menu


class TopicMenu(Menu):
    name = 'Menú de Temas'
    options = '''
    0) Menú principal
    1) Registrar
    '''

    def __init__(self):
        super(TopicMenu, self).__init__()
        self.name_topic = None

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

        self.run()

    def _ask_name(self):
        self.name_topic = input('ingrese tema: ')
