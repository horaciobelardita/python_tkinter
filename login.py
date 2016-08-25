import Tkinter as tk
import ttk
import tkMessageBox

class LoginFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        ttk.Label(self, text='LOGIN', font=('System', 14, 'bold')).grid(row=0, columnspan=2)
        ttk.Label(self, text='USUARIO', font=('System', 10, 'normal')).grid(row=1, column=0)

        self.username_input = ttk.Entry(self)
        self.username_input.grid(row=1, column=1)

        ttk.Label(self, text='CLAVE', font=('System', 10, 'normal')).grid(row=2, column=0)

        self.password_input = ttk.Entry(self, show='*')
        self.password_input.grid(row=2, column=1)

        ttk.Button(self, text='INGRESAR', command=self.login).grid(row=3, columnspan=2)

        self.pack()

    def login(self):
        username = self.username_input.get()
        if not username:
            self.username_input.focus()
            return
        password = self.password_input.get()
        if not password:
            self.password_input.focus()
            return
        if username == 'admin' and password == 'root':
            tkMessageBox.showinfo('INGRESANDO', 'ACCESO PERMITIDO')
        else:
            tkMessageBox.showerror('Incorrecto', 'ACCESO NO PERMITIDO')


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('LOGIN')
        self.resizable(False, False)
        login_frame = LoginFrame(self)


if __name__ == '__main__':
    app = App()
    app.mainloop()
