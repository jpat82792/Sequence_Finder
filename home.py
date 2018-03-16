from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import ControllerSecretary


class ViewHome:
    def __init__(self):

        frame = Tk()
        secretary = ControllerSecretary.ControllerSecretary()
        button_load_file_text = tk.StringVar()
        button_load_file_text.set("Select sequence file")
        button_load_file = Button(frame, textvariable=button_load_file_text,
                                  command=lambda: secretary.load_target_file(button_load_file_text), width=30)
        button_load_file.grid(row=1, column=1)
        label_results_file_name = Label(frame, text="Name output file and do not include file extension: ")
        label_results_file_name.grid(row=2, column=1)
        button_run_sequence_finder = Button(frame, text="Find instances of sequence", width=30, command=secretary.get_target_sequences)
        button_run_sequence_finder.grid(row=3, column=1, columnspan=2)
        entry_result_file_name = Entry(frame, width=30)
        entry_result_file_name.grid(row=2, column=2)
        frame.mainloop()



ViewHome()


