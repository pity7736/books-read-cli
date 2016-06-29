from .author_menu import AuthorMenu
from .topic_menu import TopicMenu

from .menu import Menu


class MainMenu(Menu):
    name = 'Menú Principal'
    options = '''
    0) Salir
    1) Temas
    2) Autores
    '''

    def _run_option_selected(self):
        if not self._selected_option:
            self._set_option()

        if self._selected_option == '0':
            print('Saliendo...')
            return
        elif self._selected_option == '1':
            topic_menu = TopicMenu()
            topic_menu.run()
        elif self._selected_option == '2':
            author_menu = AuthorMenu()
            author_menu.run()

        self.run()
