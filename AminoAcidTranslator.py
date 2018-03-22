import AbstractTranslator


class AminoAcidTranslator(AbstractTranslator.AbstractTranslator):
    dictionary = {"Z": "([E,Q,Z])", "J": "([L,I,J])", "B": "([D,N,B])", "X": "."}
    possible_characters = "[A-Z]"

    def __init__(self):
        self.regex = ""

    def translate_target(self, target, before, after):
        print(self.dictionary)
        print(target)
        regex = ""
        for i in range(len(target)):
            print(i)
            print(target[i])
            if target[i] is "Z" or target[i] is "J" or target[i] is "B" or target[i] is "X":
                print(self.dictionary[target[i]])
                regex += self.dictionary[target[i]]
            else:
                print(target[i])
                regex += target[i]
        print(regex)
        final = "("+self.possible_characters+"{0,"+before+"})("+regex+")("+self.possible_characters+"{0,"+after+"})"
        print(final)
        return final


    def translate(self, sequence, targetSequence):
        pass