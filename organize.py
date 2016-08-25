import Tkinter as tk
import ttk

class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.resizable(False, False)
        self.pack()
        self.master.geometry('800x600')

        self.master.bind('<Return>', self.click_ok)
        self.master.bind('<Escape>', self.click_cancel)

        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20, pady=15)
        ttk.Label(dialog_frame, text='GUI').pack()

        button_frame = tk.Frame(self)
        button_frame.pack(padx=15, pady=(0, 15))

        ttk.Button(button_frame, text='OK', default='active').pack(side=tk.RIGHT)
        ttk.Button(button_frame, text='Cancel').pack(side=tk.RIGHT)

    def click_ok(self):
        pass

    def click_cancel(self):
        pass
        
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()
