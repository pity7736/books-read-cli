from src.books_read.src.controllers import CreateAuthorController

from .menu import Menu


class AuthorMenu(Menu):
    name = 'Menú de autores'
    options = '''
    0) Menú principal
    1) Registrar
    '''

    def __init__(self):
        super(AuthorMenu, self).__init__()
        self.data = {}

    def _run_option_selected(self):
        if not self._selected_option:
            self._set_option()

        if self._selected_option == '0':
            print('Saliendo al menú principal...\n')
            return
        elif self._selected_option == '1':
            self._ask_data()
            create_controller = CreateAuthorController(**self.data)
            create_controller.save()
            print('Tema registrado exitosamente.\n')

        self.run()

    def _ask_data(self):
        first_name = input('Ingrese nombre: ')
        last_name = input('Ingrese apellido: ')
        self.data['first_name'] = first_name
        self.data['last_name'] = last_name
