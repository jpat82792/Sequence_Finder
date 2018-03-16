from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import re

class ControllerSecretary:

    def __init__(self):
        print("init secretary")
        self.target_file_path = ""
        self.regex_expression = "([A-Z]{0,10})(K...W)([A-Z]{0,10})"
        self.compiled_regex = re.compile(self.regex_expression)
        self.result_file_name = "Sequence result file"
        self.result_file_extension = ".txt"

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
        return str.split(file_path,"/")[-1]

    def open_file(self):
        file = open(self.target_file_path, 'r')
        if file.mode == 'r':
            file_content = file.read()
            return file_content
        else:
            return

    def nucleotide_target_sequence_regex_convert(self, target_sequence):
        regexable_string = target_sequence.replace("N", ".")

    def amino_acid_target_sequence_regex_convert(self, target_sequence):
        regexable_string = target_sequence.replace("X", ".")

    def write_target_sequences_to_file(self, matches, output_file_name):
        matches_length = len(matches)
        results_file = open(output_file_name + self.result_file_extension, "w+")
        for i in range(matches_length):
            inner_length = len(matches[i])
            for j in range(inner_length):
                results_file.write(matches[i][j]+"   ")
            results_file.write('\n')

    def get_target_sequences(self, file_name):
        file = self.open_file()
        print(file)
        matches = self.compiled_regex.findall(file)
        print(matches)
        self.write_target_sequences_to_file(matches=matches, output_file_name=file_name)
