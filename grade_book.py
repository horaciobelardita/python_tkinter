import Tkinter as tk
import ttk
import tkMessageBox, tkFileDialog

# file format
# student name, grade, grade

class AddNamesFrame(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='CREAR ALUMNOS').pack()
        input_frame = ttk.Frame(self)
        ttk.Label(input_frame, text='Nombre').grid(row=0, column=0)
        self.name_input = ttk.Entry(input_frame)
        self.name_input.grid(row=0, column=1)
        ttk.Button(input_frame, text='Agregar', command=self.add).grid(columnspan=2, row=1)
        self.listbox = tk.Listbox(input_frame)
        self.listbox.grid(row=2, columnspan=2)
        ttk.Button(input_frame, text='Guardar', command=self.save).grid(row=3, columnspan=2)
        ttk.Button(input_frame, text='Volver a menu', command=self.back_to_menu).grid(row=4, columnspan=2)
        input_frame.pack()
        self.controller = controller
        self.new = True

    def back_to_menu(self):
        if self.new:
            confirm = tkMessageBox.askyesno('Salir', 'Desea guardar los cambios antes de salir')
            if confirm == tk.YES:
                self.save()
        self.controller.show_frame(MenuFrame)

    def add(self):
        # obtengo el nombre ingresado en el Entry
        name = self.name_input.get()
        if name:
            # elimino el contenido del Entry
            self.name_input.delete(0, tk.END)
            # inserto el nombre ingresado en el listbox
            self.listbox.insert(tk.END, name)
        else:
            tkMessageBox.showerror('Error', 'Debe ingresar un nombre')
        self.name_input.focus()

    def save(self):
        filename = tkFileDialog.asksaveasfilename()
        if filename:
            with open(filename, 'w') as f:
                # grabo el nombre del archivo en la primer linea
                f.write(filename.split('/')[-1] + '\n')
                # recorro el listbox y almaceno cada nombre en una linea diferente
                for i in range(self.listbox.size()):
                    item = self.listbox.get(i)
                    f.write(item + '\n')
            # eliminar los elementos del listbox
            self.listbox.delete(0, tk.END)
            tkMessageBox.showinfo('Exito', 'Archivo Guardado con exito')
            self.new = False
        self.controller.show_frame(MenuFrame)


class MenuFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text='LIBRO DE NOTAS', font=('System', 14, 'bold')).pack()
        ttk.Button(self, text='Crear', command=self.create).pack(pady=10)
        self.add_button = ttk.Button(self, text='Agregar', command=self.add, state='disabled')
        self.add_button.pack(pady=10)
        self.show_button = ttk.Button(self, text='Ver', command=self.show, state='disabled')
        self.show_button.pack(pady=10)
        self.delete_grade_btn = ttk.Button(self, text='Eliminar Nota', command=self.delete_grade, state='disabled')
        self.delete_grade_btn.pack(pady=10)
        self.delete_student_btn = ttk.Button(self, text='Eliminar Alumno', command=self.delete_student, state='disabled')
        self.delete_student_btn.pack(pady=10)
        ttk.Button(self, text='Salir', command=controller.destroy).pack(pady=10)
        self.controller = controller
        self.pack()

    def add(self):
        pass

    def show(self):
        pass

    def create(self):
        self.controller.show_frame(AddNamesFrame)
        for b in (self.add_button, self.show_button, self.delete_grade_btn, self.delete_student_btn):
            b.config(state='active')

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
        # configuracion basica(minimum, maximum)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for f in (MenuFrame, AddNamesFrame):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(column=0, row=0, sticky='nsew')

        self.show_frame(MenuFrame)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


if __name__ == '__main__':
    app = App()
    app.mainloop()
