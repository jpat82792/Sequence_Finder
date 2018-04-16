import AbstractTranslator


class AminoAcidTranslator(AbstractTranslator.AbstractTranslator):
    dictionary = {"Z": "([E,Q,Z])", "J": "([L,I,J])", "B": "([D,N,B])", "X": "."}
    possible_characters = "[A-Z]"

    def __init__(self):
        super().__init__(dictionary=self.dictionary, possible_characters=self.possible_characters)

    def translate_target(self, target, beforeTarget, afterTarget):
        return super().translate_target(target=target, beforeTarget=beforeTarget, afterTarget=afterTarget)
