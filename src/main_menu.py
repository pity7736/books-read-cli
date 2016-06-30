from .author_menu import AuthorMenu
from .book_menu import BookMenu
from .topic_menu import TopicMenu

from .menu import Menu


class MainMenu(Menu):
    name = 'Menú Principal'
    options = '''
    0) Salir
    1) Temas
    2) Autores
    3) Libros
    '''

    def _run_selected_option(self):
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
        elif self._selected_option == '3':
            book_menu = BookMenu()
            book_menu.run()
        else:
            print('opción inválida.')

        self.run()
