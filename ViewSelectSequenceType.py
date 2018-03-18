from tkinter import *


class ViewSelectSequenceType:
    sequence_type_list = ["nucleotide", "amino acid"]

    def __init__(self, main_frame):
        current_parent = LabelFrame(main_frame)
        current_parent.pack()
        current_parent.place(relheight=1, relwidth=1)
        listbox_sequence_type_list = Listbox(current_parent)
        self.__init_listbox(listbox=listbox_sequence_type_list)
        listbox_sequence_type_list.pack()
        listbox_sequence_type_list.place(bordermode=INSIDE, relheight=0.1, relwidth=0.5, relx=0.25, rely=0.1)
        self.__init_main_label(current_parent=current_parent)
        self.__init_next_button(current_parent=current_parent)

    def __init_listbox(self, listbox):
        listbox_content_length = len(self.sequence_type_list)
        for i in range(listbox_content_length):
            listbox.insert(i, self.sequence_type_list[i])

    def __init_main_label(self, current_parent):
        label = Label(text="Sequence Type", font=(None, 50))
        label.pack()
        label.place(bordermode=INSIDE, relheight=0.1, relwidth=0.5, relx=0.25, rely=0.0)

    def __init_next_button(self, current_parent):
        button = Button(text="NEXT", font=(None, 50))
        button.pack()
        button.place(bordermode=INSIDE, relheight=0.1, relwidth=0.5, relx=0.25, rely=0.2)
