from src.books_read.src.controllers.create_topic import CreateTopicController


class TopicMenu:

    def __init__(self):
        self.option = None
        self.name_topic = None

    def run(self):
        self._show()
        self._set_option()
        self._run_option_selected()

    @staticmethod
    def _show():
        print('Menú de temas')
        print('''
            0) Salir
            1) Registrar
        ''')

    def _set_option(self):
        self.option = input('seleccione opción: ')

    def _run_option_selected(self):
        if not self.option:
            return self._set_option()

        if self.option == '0':
            return
        elif self.option == '1':
            self._ask_name()
            create_controller = CreateTopicController(self.name_topic)
            create_controller.save()
            print('Tema registrado exitosamente.')

        self.run()

    def _ask_name(self):
        self.name_topic = input('ingrese tema: ')
