from ..commands import ExitCommand, CreateAuthorCommand
from .menu import Menu


class AuthorMenu(Menu):

    def _get_options(self):
        self.exit_command = ExitCommand('Menú principal')
        commands = (
            self.exit_command,
            CreateAuthorCommand('Registrar')
        )
        return commands
