import Tkinter as tk
import ttk
import tkMessageBox, tkFileDialog

# file format
# student name, grade, grade


class GradeFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('GRADE BOOK')
        self.resizable(False, False)
        login_frame = LoginFrame(self)


if __name__ == '__main__':
    app = App()
    app.mainloop()
