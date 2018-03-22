class NucleotideTranslator:
    dictionary = {"R": "[A,G,R]", "Y": "[C,T,U,Y]", "K": "[G,T,U,K,]", "M": "[A,C,M]", "S": "[C,G]", "W": "[A,T,U,W]",
                  "B": "[C,G,T,U]", "D": "[A,G,T,U]", "H": "[A,C,T,U]", "V": "[A,C,G]", "N": "."}
    def __init__(self):
        pass

    def translate_target(self, target, before, after):
        print(self.dictionary)
        print(target)
        regex = ""
        for i in range(len(target)):
            print(i)
            print(target[i])
            if target[i] is "R" or target[i] is "Y" or target[i] is "K" or target[i] is "M" or target[i] is "S" \
                    or target[i] is "W" or target[i] is "B" or target[i] is "D" or target[i] is "H" or target[i] is "V" \
                    or target[i] is "N":
                print(self.dictionary[target[i]])
                regex += self.dictionary[target[i]]
            else:
                print(target[i])
                regex += target[i]
        print(regex)
        final = "("+self.possible_characters+"{0,"+before+"})("+regex+")("+self.possible_characters+"{0,"+after+"})"
        print(final)
        return final