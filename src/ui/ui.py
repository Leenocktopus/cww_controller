import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

from src.service.model import input_lvs
from src.service.service import Service


class UI:

    def __init__(self, root, service: Service):
        self.root = root
        self.service = service
        self.save_button = tk.Button(root, font=('Arial', 14), text="Save", width=20, command=self.save)
        self.view_results_button = tk.Button(root, font=('Arial', 14), text="View Rating", width=20,
                                             command=self.view_rating)

        self.vars = [StringVar(root), StringVar(root, ''), StringVar(root, ''), StringVar(root, '')]

        Label(root, text="Select employee you are rating: ", font='Helvetica 18 bold') \
            .grid(column=0, row=0, columnspan=2, sticky=W, padx=(10, 0))

        options = OptionMenu(root, self.vars[0], *self.service.find_all_names())
        options.config(width=13)
        options.grid(column=2, row=0, sticky=W)

        row = 1
        for index, input_lv in enumerate(input_lvs):
            Label(root, text=input_lv['name'], font='Helvetica 18 bold') \
                .grid(column=0, row=row, columnspan=5, sticky=W, padx=(10, 0))
            row = row + 1
            for term in input_lv['terms']:
                Radiobutton(root, text=term, variable=self.vars[index + 1], value=term) \
                    .grid(column=0, row=row, sticky=W, padx=(25, 0), columnspan=5)
                row = row + 1

        self.save_button.grid(row=row, column=0, columnspan=5, pady=(2, 1))
        self.view_results_button.grid(row=row + 1, column=0, columnspan=5, pady=(2, 1))

    def view_rating(self):
        ratings_window = Toplevel(self.root)
        ratings_window.title("Rating")
        ratings_window.geometry("460x595")
        treeview = Treeview(ratings_window, selectmode='browse', show='headings', columns=("1", "2", "3", "4"),
                            height=31)
        treeview.grid(row=0, column=0)
        scroll = Scrollbar(ratings_window, orient="vertical", command=treeview.yview)
        scroll.grid(row=0, column=1, sticky=NS)
        treeview.configure(xscrollcommand=scroll.set)

        treeview.heading("1", text="Number")
        treeview.heading("2", text="Name")
        treeview.heading("3", text="Rating")
        treeview.heading("4", text="Decision")

        treeview.column("1", width=110, anchor='c')
        treeview.column("2", width=110, anchor='c')
        treeview.column("3", width=110, anchor='c')
        treeview.column("4", width=110, anchor='c')

        for index, row in enumerate(self.service.find_all_ratings()):
            treeview.insert("", 'end', text="L1", values=(index + 1, row[0], round(float(row[1]), 4), row[2]))

    def save(self):
        if self.vars[0].get() == '' or self.vars[1].get() == '' or self.vars[2].get() == '' or self.vars[3].get() == '':
            messagebox.showerror('Error', 'Please fill every field in the form to save rating')
            return
        rating, decision = self.service.save_rating(self.vars[0].get(),
                                                    [self.vars[1].get(), self.vars[2].get(), self.vars[3].get()])
        messagebox.showinfo('Result', 'Result is:\n{rating} - {decision}'.format(rating=rating, decision=decision))
