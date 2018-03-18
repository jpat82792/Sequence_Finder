from tkinter import *
import AbstractScreen


class ViewSelectSequenceType(AbstractScreen.AbstractScreen):
    sequence_type_list = ["nucleotide", "amino acid"]
    ui_elements = []

    def __init__(self, main_frame, home):
        self.current_parent = LabelFrame(main_frame)
        self.current_parent.pack()
        self.current_parent.place(relheight=1, relwidth=1)
        self.ui_elements.append(self.current_parent)
        self.listbox_sequence_type_list = Listbox(self.current_parent)
        self.__init_listbox(listbox=self.listbox_sequence_type_list)
        self.listbox_sequence_type_list.pack()
        self.listbox_sequence_type_list.place(bordermode=INSIDE, relheight=0.1, relwidth=0.5, relx=0.25, rely=0.1)
        self.ui_elements.append(self.listbox_sequence_type_list)
        label = Label(text="Sequence Type", font=(None, 50))
        label.pack()
        label.place(bordermode=INSIDE, relheight=0.1, relwidth=0.5, relx=0.25, rely=0.0)
        self.ui_elements.append(label)
        self.button = Button(text="NEXT", font=(None, 50), command= self.next_screen)
        self.button.pack()
        self.ui_elements.append(self.button)
        self.__init_next_button(current_parent=self.current_parent, main_frame=main_frame, home=home, button=self.button)

    def __init_listbox(self, listbox):
        listbox_content_length = len(self.sequence_type_list)
        for i in range(listbox_content_length):
            listbox.insert(i, self.sequence_type_list[i])

    def __init_next_button(self, current_parent, main_frame, home, button):
        button.place(bordermode=INSIDE, relheight=0.1, relwidth=0.5, relx=0.25, rely=0.2)

    def pack(self):
        for element in self.ui_elements:
            element.pack()

    def next_screen(self):
        print(self.current_parent)
        self.current_parent.pack_forget()
