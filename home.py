from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import ControllerSecretary


class ViewHome:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        secretary = ControllerSecretary.ControllerSecretary()
        button_load_file_text = tk.StringVar()
        button_load_file_text.set("Select sequence file")
        button_load_file = Button(frame, textvariable=button_load_file_text,
                                  command=lambda: secretary.load_target_file(button_load_file_text), width=30)
        button_load_file.pack(side=LEFT, fill=X)
        label_enter_finder_sequence = Label(frame, text="Search Sequence", width=30)
        label_enter_finder_sequence.pack(side=BOTTOM)
        entry_target_sequence = Entry(frame, width=30)
        entry_target_sequence.pack(side=BOTTOM)
        button_run_sequence_finder = Button(frame, text="Find instances of sequence", width=30, command=secretary.get_target_sequences)
        button_run_sequence_finder.pack(side=RIGHT)

root = Tk()

ViewHome(root)
root.mainloop()

