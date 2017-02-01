from ..commands import ExitCommand, CreateBookCommand
from .menu import Menu


class BookMenu(Menu):

    def _get_options(self):
        self.exit_command = ExitCommand('Menú principal')
        commands = (
            self.exit_command,
            CreateBookCommand('Registrar')
        )
        return commands
