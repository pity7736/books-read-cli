from .author_menu_command import AuthorMenuCommand
from .book_menu_command import BookMenuCommand
from ..commands import ExitCommand
from .menu import Menu
from .topic_menu_command import TopicMenuCommand


class MainMenu(Menu):

    def _get_options(self):
        self.exit_command = ExitCommand()
        commands = (
            self.exit_command,
            TopicMenuCommand('Temas'),
            AuthorMenuCommand('Autores'),
            BookMenuCommand('Libros')
        )
        return commands
