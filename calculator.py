# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
import sys


root = tk.Tk()
root.title('Calculadora')

class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid(column=0, row=0, padx=15, pady=10)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.user_input = ttk.Entry(self)
        self.user_input.grid(column=1, row=1, columnspan=5)
        


app = App(root)
root.mainloop()
