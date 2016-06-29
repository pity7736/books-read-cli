from abc import ABCMeta, abstractmethod


class Menu(metaclass=ABCMeta):
    name = ''
    options = ''

    def __init__(self):
        self.option_selected = None

    def run(self):
        self._show()
        self._set_option()
        self._run_option_selected()

    def _show(self):
        print(self.name)
        print(self.options)

    def _set_option(self):
        self.option_selected = input('seleccione opción: ')

    @abstractmethod
    def _run_option_selected(self):
        pass
