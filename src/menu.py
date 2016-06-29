from abc import ABCMeta, abstractmethod


class Menu(metaclass=ABCMeta):
    name = ''
    options = ''

    def __init__(self):
        self._selected_option = None

    def run(self):
        self._show()
        self._set_option()
        self._run_option_selected()

    def _show(self):
        print(self.name)
        print(self.options)

    def _set_option(self):
        self._selected_option = input('seleccione opción: ')

    @abstractmethod
    def _run_option_selected(self):
        pass
