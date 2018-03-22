from abc import ABC, abstractmethod


class AbstractTranslator:

    @abstractmethod
    def translate(self, sequence, targetSequence, beforeTarget, afterTarget):
        pass
