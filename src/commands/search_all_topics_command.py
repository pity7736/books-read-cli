from .search_topic_command import SearchTopicCommand


class SearchAllTopicCommand(SearchTopicCommand):

    def _get_topics(self):
        self.topics = self.search_controller.get_all()

