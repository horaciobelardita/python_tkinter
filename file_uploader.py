import Tkinter as tk
import ttk
import tkFileDialog
import time


class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.resizable(False, False)
        self.master.geometry('640x480')
        self.pack()

        file_frame = tk.Frame(self)
        file_frame.pack(padx=20, pady=15)
        self.file_button = tk.Button(file_frame, text='Seleccionar archivos', command=self.file_picker)
        self.file_button.pack(side=tk.RIGHT)


        self.file_count = tk.StringVar()
        self.file_label = ttk.Label(file_frame, textvariable=self.file_count)
        self.file_label.pack(side=tk.RIGHT)

        ttk.Label(self, text="Agregar Comentario").pack(padx=15, pady=15)

        text_frame = tk.Frame(self, borderwidth=1, relief='sunken')
        text_frame.pack(padx=15, pady=15)

        self.text = tk.Text(text_frame, width=30, height=4, bg='#ffffff', wrap=tk.WORD, font=('System', 14))
        self.text.focus_set()
        self.text.pack()

        button_frame = tk.Frame(self)
        button_frame.pack(padx=15, pady=15)

        self.submit_button = ttk.Button(button_frame, text='Enviar', state='disabled', command=self.click_submit)
        self.submit_button.pack(side=tk.RIGHT)

        self.cancel_button = ttk.Button(button_frame, text='Cancelar', command=self.click_cancel)
        self.cancel_button.pack(side=tk.RIGHT)

    def click_cancel(self):
        self.master.destroy()

    def click_submit(self):
        comment = self.text.get('1.0', tk.END)
        if comment.rstrip():
            print comment.rstrip()
        if self.selected_files:
            loading = LoadingFrame(self.master, len(self.selected_files))
            self.toggle_state('disabled')
            for path in self.selected_files:
                loading.progress['value'] += 1
                self.update()
                time.sleep(2)
                with open(path) as f:
                    print "Archivo abierto: {}: {}".format(path, f)
            loading.destroy()
            self.toggle_state('normal')

    def toggle_state(self, state):
        state = state if state in ['normal', 'disabled'] else 'normal'
        widgets = (self.file_button, self.file_label, self.text, self.submit_button, self.cancel_button)
        for widget in widgets:
            widget.configure(state=state)


    def file_picker(self):
        self.selected_files = tkFileDialog.askopenfilenames(parent=self)
        self.file_count.set("{} archivos".format(len(self.selected_files)))
        self.submit_button.config(state='active')

class LoadingFrame(tk.Frame):

    def __init__(self, master, count):
        tk.Frame.__init__(self, master, borderwidth=5, relief='groove')
        self.pack()

        ttk.Label(self, text='Subiendo archivos....').pack(padx=15, pady=10)
        self.progress = ttk.Progressbar(self, orient='horizontal', length=250, mode='determinate')
        self.progress.pack(padx=15, pady=10)
        self.progress['value'] = 0
        self.progress['maximum'] = count

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()
