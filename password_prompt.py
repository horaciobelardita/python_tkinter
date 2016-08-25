import Tkinter as tk
import ttk

class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.resizable(False, False)
        self.master.geometry('640x480')
        self.pack()

        tk.Message(self, text='Autenticarse con usuario y password \
        antes de continuar', font='System 14 bold', justify='center', aspect=800)\
        .pack(pady=15)

        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20, pady=15)
        # Username input
        ttk.Label(dialog_frame, text='USUARIO').grid(row=0, column=0)
        self.user_input = ttk.Entry(dialog_frame, width=24)
        self.user_input.grid(row=0, column=1)
        self.user_input.focus_set()
        # Password input
        ttk.Label(dialog_frame, text='CLAVE').grid(row=1, column=0)
        self.pass_input = ttk.Entry(dialog_frame, width=24, show='*')
        self.pass_input.grid(row=1, column=1)
        # Button group
        button_frame = tk.Frame(self)
        button_frame.pack(padx=15, pady=(0, 15))
        ttk.Button(button_frame, text='OK', default='active').pack(side=tk.RIGHT)
        ttk.Button(button_frame, text='Cancel').pack(side=tk.RIGHT)

    def click_ok(self):
        print "USARIO: {}\nCLAVE:{}".format(self.user_input.get(), self.pass_input.get())


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()
