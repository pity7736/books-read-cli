from ..commands import Command
from .topic_menu import TopicMenu


class TopicMenuCommand(Command):

    def execute(self):
        topic_menu = TopicMenu()
        topic_menu.run()
