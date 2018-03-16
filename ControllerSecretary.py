from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import re

class ControllerSecretary:

    def __init__(self):
        print("init secretary")
        self.target_file_path = ""
        self.regex_expression = "([A-Z]{0,10})(K...W)([A-Z]{0,10})"
        self.compiled_regex = re.compile(self.regex_expression)


    def load_target_file(self, buttonStringVar):
        file_name = askopenfilename(filetype=(("FASTA","*.fasta"), ("All files", "*.*")))

        if file_name:
            try:
                self.target_file_path = file_name
                print(self.target_file_path)
                buttonStringVar.set(self.get_file_name(file_name))

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

    def get_target_sequences(self):
        file = self.open_file()
        print(file)
        matches = self.compiled_regex.search(file)
        print(matches)
