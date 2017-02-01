from abc import ABCMeta, abstractmethod


class Menu(metaclass=ABCMeta):

    def __init__(self):
        self._commands = []
        self._set_options()

    def _set_options(self):
        options = self._get_options()
        self._commands.extend(options)

    @abstractmethod
    def _get_options(self):
        pass

    def run(self):
        self._show()
        option = self._get_option()
        self._commands[option].execute()

    def _show(self):
        print()
        print('-' * 50)
        for i, command in enumerate(self._commands):
            print('{}) {}'.format(i, command.get_title()))
        print('-' * 50)

    def _get_option(self):
        while True:
            try:
                option = int(input('Digite opción: '))
            except ValueError:
                print('Ingrese un número')
            else:
                if 0 <= option < len(self._commands):
                    break
                print('Opción inválida')

        return option
