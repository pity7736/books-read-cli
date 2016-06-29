from .topic_menu import TopicMenu

from .menu import Menu


class MainMenu(Menu):
    name = 'Menú Principal'
    options = '''
    0) Salir
    1) Temas
    '''

    def _run_option_selected(self):
        if not self.option_selected:
            self._set_option()

        if self.option_selected == '0':
            print('Saliendo...')
            return
        elif self.option_selected == '1':
            topic_menu = TopicMenu()
            topic_menu.run()

        self.run()
