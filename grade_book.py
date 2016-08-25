import Tkinter as tk
import ttk
import tkMessageBox, tkFileDialog

# file format
# student name, grade, grade

class AddNameFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text='CREAR ALUMNOS').grid(row=0, columnspan=2)



class GradeFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text='LIBRO DE NOTAS', font=('System', 14, 'bold')).pack()
        ttk.Button(self, text='Crear', command=self.create).pack(pady=10)
        ttk.Button(self, text='Agregar', command=self.add, state='disabled').pack(pady=10)
        ttk.Button(self, text='Ver', command=self.show, state='disabled').pack(pady=10)
        ttk.Button(self, text='Eliminar Nota', command=self.delete_grade, state='disabled').pack(pady=10)
        ttk.Button(self, text='Eliminar Alumno', command=self.delete_student, state='disabled').pack(pady=10)
        ttk.Button(self, text='Salir', command=controller.destroy).pack(pady=10)
        self.pack()

    def add(self):
        pass

    def show(self):
        pass

    def create(self):
        _file = tkFileDialog.asksaveasfile()
        if _file:
            names = []

    def delete_grade(self):
        pass

    def delete_student(self):
        pass


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('GRADE BOOK')
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # minimum, maximum
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = GradeFrame(container, self)
        self.frames[GradeFrame] = frame

        frame.grid(column=0, row=0)
        self.show_frame(GradeFrame)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


if __name__ == '__main__':
    app = App()
    app.mainloop()
