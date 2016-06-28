from src.topic_menu import TopicMenu


class MainMenu:

    def __init__(self):
        self.option = None

    def run(self):
        self._show()
        self._set_option()
        self._run_option_selected()

    @staticmethod
    def _show():
        print("Books Read Menú")
        print("""
            0) Salir
            1) Temas
        """)

    def _set_option(self):
        self.option = input('seleccione opción: ')

    def _run_option_selected(self):
        if not self.option:
            return self._set_option()

        if self.option == '0':
            return
        elif self.option == '1':
            topic_menu = TopicMenu()
            topic_menu.run()

        self.run()
