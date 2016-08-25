import Tkinter as tk
import ttk

LARGE_FONT = ('System', 14)


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # minimum, maximum
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = StartPage(container, self)

        self.frames[StartPage] = frame
        frame.grid(row=0, column=0)

        self.show_frame(StartPage)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text='Start Page', font=LARGE_FONT).pack(padx=10, pady=10)
        

if __name__ == '__main__':
    app = App()
    app.mainloop()
