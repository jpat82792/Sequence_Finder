from abc import ABC, abstractclassmethod


class AbstractScreen(ABC):

    @abstractclassmethod
    def next_screen(self, root_screen):
        pass
