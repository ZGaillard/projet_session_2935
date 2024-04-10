from tkinter import Frame, StringVar, LEFT, W, YES

import ttkbootstrap as ttk


class SearchableTable(ttk.Treeview):

    def __init__(self, parent, data, combobox=True):

        self.combobox = combobox
        # Search bar and combobox for column selection
        search_bar_container = Frame(parent)
        search_bar_container.pack(pady=20)

        self.search_text = StringVar()
        search_bar = ttk.Entry(
            search_bar_container,
            textvariable=self.search_text,
            width=40
        )
        search_bar.pack(side=LEFT, padx=10)

        self.search_text.trace(
            "w",
            lambda *args: self.search()
        )

        self.tuples = data.get_tuples()

        if combobox:
            self.search_combobox_value = StringVar()
            self.search_combobox = ttk.Combobox(
                search_bar_container,
                textvariable=self.search_combobox_value,
                values=data.get_column_names(),
                state='readonly', width=15
            )
            self.search_combobox.current(0)
            self.search_combobox.pack(side=LEFT, padx=10)

            self.search_combobox.bind(
                "<<ComboboxSelected>>",
                lambda *args: self.search()
            )

        self.parent = parent
        self.data = data.get_tuples()

        self.column_names = data.get_column_names()
        ttk.Treeview.__init__(
            self, parent,
            columns=self.column_names,
            show="headings"
        )

        # determine the width of the columns based on the data
        for i, column_name in enumerate(self.column_names):
            mean_width = sum(
                len(str(row[i + 1])) for row in self.data
            ) // len(self.data)
            self.column(column_name, width=mean_width * 32,
                        minwidth=100, stretch=YES
                        )
            self.heading(column_name, text=column_name, anchor=W)

        # insert data (skip the first column which is the id)
        for row in self.data:
            visible_row = row[1:]
            self.insert("", "end", values=visible_row)

    def search(self):
        self.reset()
        search_text = self.search_text.get().lower()
        if self.combobox:
            search_column = self.search_combobox.get()
        else:
            search_column = self.column_names[0]
        search_index = self.column_names.index(search_column)
        for row in self.data:
            visible_row = row[1:]
            if search_text in str(visible_row[search_index]).lower():
                self.insert("", "end", values=visible_row)

    def reset(self):
        x = self.get_children()
        for item in x:
            self.delete(item)

    def get_selected_row(self):
        selected_row = self.item(self.selection()[0])
        for row in self.data:
            if row[1:] == selected_row['values']:
                return row
        return None
