from abc import ABC, abstractmethod


class AbstractTranslator:

    def __init__(self, dictionary, possible_characters):
        self.regex = ""
        self.dictionary = dictionary
        self.possible_characters = possible_characters

    @abstractmethod
    def translate_target(self, target, beforeTarget, afterTarget):
        print("abs translate_target")
        regex = ""
        for i in range(len(target)):
            matching_char = ""
            matched_dictionary = False
            for key in self.dictionary:
                if target[i] is key:
                    matched_dictionary = True
                    matching_char = target[i]
            if matched_dictionary:
                regex += self.dictionary[matching_char]
            else:
                regex += target[i]
        final = "(" + self.possible_characters + "{0," + beforeTarget + "})(" + regex + ")(" + self.possible_characters + "{0," + afterTarget + "})"
        print(final)
        return final
