from .command import Command
from ..books_read.src.controllers.search_topics import SearchTopicsController


class SearchTopicCommand(Command):

    def __init__(self, title):
        super(SearchTopicCommand, self).__init__(title=title)
        self.topics = None
        self.search_controller = SearchTopicsController()

    def execute(self):
        self._get_topics()
        return self._show_result()

    def _get_topics(self):
        topic_name = input('Ingrese nombre de tema: ')
        self.topics = self.search_controller.filter_by_name(topic_name)

    def _show_result(self):
        if self.topics.count():
            print('\nListado de temas')
            for topic in self.topics:
                print(topic.name)
        else:
            print('No hay resultados.')
