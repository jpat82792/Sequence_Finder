from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import re
import AminoAcidTranslator
import NucleotideTranslator
import os

'''
The secretary can create and modify ModelSequenceQuery
'''


class ControllerSecretary:
    sequence_type = ""
    target_sequence = ""
    before_target_sequence = ""
    after_target_sequence = ""
    output_file_path = ""
    output_file_name = ""
    target_file_name = ""

    def __init__(self):
        print("init secretary")
        self.target_file_path = ""
        self.regex_expression = "([A-Z]{0,10})(K...W)([A-Z]{0,10})"
        self.compiled_regex = None
        self.result_file_name = "Sequence result file"
        self.result_file_extension = ".txt"
        self.amino_acid_translator = AminoAcidTranslator.AminoAcidTranslator()
        self.nucleotide_translator = AminoAcidTranslator.AminoAcidTranslator()

    def load_target_file(self, button_string_var):
        file_name = askopenfilename()

        if file_name:
            try:
                self.target_file_path = file_name
                print(self.target_file_path)
                button_string_var.set(self.get_file_name(file_name))

            except:
                showerror("Opening Sequence File", "Failed to read file \n '%s'" % file_name)
            return

    def get_file_name(self, file_path):
        return str.split(file_path, "/")[-1]

    def open_file(self):
        actual_path = os.path.join(self.target_file_path, self.target_file_name)
        file = open(actual_path, 'r')
        if file.mode == 'r':
            file_content = file.read()
            return file_content
        else:
            return

    def nucleotide_target_sequence_regex_convert(self, target_sequence):
        regexable_string = target_sequence.replace("N", ".")

    def amino_acid_target_sequence_regex_convert(self, target_sequence):
        regexable_string = target_sequence.replace("X", ".")

    def write_target_sequences_to_file(self, matches):
        results_file = open(os.path.join(self.output_file_path, self.output_file_name), "w+")
        for match in matches:
            print(match)
            print(match.span()[0])
            print(match.groups())
            results_file.write(str(match.span()[0]) + "   " + str(match.span()[1])+ "   ")
            current_group = match.groups()
            for i in range(len(current_group)):
                results_file.write(current_group[i] + "   ")
            results_file.write('\n')

    def get_target_sequences(self, ):
        file = self.open_file()
        self.compiled_regex = re.compile(self.regex_expression)
        matches = self.compiled_regex.finditer(file)
        print(matches)
        self.write_target_sequences_to_file(matches=matches)

    def translate_target(self):
        print("translate_target()")
        print(self.target_file_name)
        actual_path = os.path.join(self.target_file_path, self.target_file_name)
        print(actual_path)
        if self.sequence_type == "Amino Acid":
            self.regex_expression = self.amino_acid_translator.translate_target(self.target_sequence,
                                                                                self.before_target_sequence,
                                                                                self.after_target_sequence)
            print(self.regex_expression)
        else:
            self.regex_expression = self.nucleotide_translator.translate_target(self.target_sequence,
                                                                                self.before_target_sequence,
                                                                                self.after_target_sequence)
            print(self.regex_expression)
