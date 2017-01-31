from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):

    def __init__(self, title):
        self._title = title

    def get_title(self):
        return self._title

    @abstractmethod
    def execute(self):
        pass
