import AbstractTranslator


class NucleotideTranslator(AbstractTranslator.AbstractTranslator):
    dictionary = {"R": "[A,G,R]", "Y": "[C,T,U,Y]", "K": "[G,T,U,K,]", "M": "[A,C,M]", "S": "[C,G]", "W": "[A,T,U,W]",
                  "B": "[C,G,T,U]", "D": "[A,G,T,U]", "H": "[A,C,T,U]", "V": "[A,C,G]", "N": "."}
    possible_characters = "[A-Z]"

    def __init__(self):
        super().__init__(dictionary=self.dictionary, possible_characters=self.possible_characters)

    def translate_target(self, target, before, after):
        return super().translate_target(target=target, beforeTarget=before, afterTarget=after)
