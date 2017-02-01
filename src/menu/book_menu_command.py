from ..commands import Command
from .book_menu import BookMenu


class BookMenuCommand(Command):

    def execute(self):
        book_menu = BookMenu()
        book_menu.run()
