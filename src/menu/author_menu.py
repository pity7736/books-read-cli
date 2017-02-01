from ..commands import ExitCommand, CreateAuthorCommand
from .menu import Menu


class AuthorMenu(Menu):
    name = 'Menú de autores'
    options = '''
    0) Menú principal
    1) Registrar
    '''

    def _get_options(self):
        self.exit_command = ExitCommand('Menú principal')
        commands = (
            self.exit_command,
            CreateAuthorCommand('Registrar')
        )
        return commands
