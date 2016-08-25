import Tkinter as tk
import ttk

LARGE_FONT = ('Verdana', 12)


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # cambiar el tamanio de la ventana
        self.geometry('800x600')
        # contenedor para los demas frames
        container = ttk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # configuracion basica(minimum, maximum)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # diccionario para cambiar entre multiples frames
        self.frames = {}

        for f in (StartPage, PageOne, PageTwo):

            frame = f(container, self)

            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

class PageOne(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Page One', font=LARGE_FONT).pack(padx=10, pady=10)
        ttk.Button(self, text='Visit page 2',
        command=lambda: controller.show_frame(PageTwo)).pack()
        ttk.Button(self, text='Back to Home',
        command=lambda: controller.show_frame(StartPage)).pack()

class PageTwo(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Page Two', font=LARGE_FONT).pack(padx=10, pady=10)
        ttk.Button(self, text='Visit Page 1',
        command=lambda: controller.show_frame(PageOne)).pack()
        ttk.Button(self, text='Back to Home',
        command=lambda: controller.show_frame(StartPage)).pack()


class StartPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Start Page', font=LARGE_FONT).pack(padx=10, pady=10)
        ttk.Button(self, text='Visit Page 1',
                command=lambda: controller.show_frame(PageOne)).pack()

if __name__ == '__main__':
    app = App()
    app.mainloop()
