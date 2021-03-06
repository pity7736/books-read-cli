from .command import Command


class ExitCommand(Command):

    def __init__(self, title='Salir'):
        super(ExitCommand, self).__init__(title)
        self._close = False

    def execute(self):
        self._close = True

    def is_closed(self):
        return self._close
