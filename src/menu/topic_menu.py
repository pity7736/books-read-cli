from ..commands import ExitCommand, CreateTopicCommand, SearchTopicCommand,\
    SearchAllTopicCommand
from .menu import Menu


class TopicMenu(Menu):

    def _get_options(self):
        self.exit_command = ExitCommand('Menú principal')
        commands = (
            self.exit_command,
            CreateTopicCommand('Registrar'),
            SearchTopicCommand('Buscar por nombre'),
            SearchAllTopicCommand('Listar todos los temas')
        )
        return commands
