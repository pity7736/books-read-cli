from .author_menu import AuthorMenu
from ..commands import Command


class AuthorMenuCommand(Command):

    def execute(self):
        author_menu = AuthorMenu()
        author_menu.run()
