from ..commands import ExitCommand
from .menu import Menu
from .topic_menu_command import TopicMenuCommand


class MainMenu(Menu):

    def _get_options(self):
        self.exit_command = ExitCommand()
        commands = (
            self.exit_command,
            TopicMenuCommand('Temas')
        )
        return commands

    def run(self):
        while self.exit_command.is_closed() is False:
            super(MainMenu, self).run()
