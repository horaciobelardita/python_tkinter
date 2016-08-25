import Tkinter as tk
import ttk

class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.resizable(False, False)
        self.pack()
        self.master.geometry('800x600')
        self.master.title('Title')

        # Buttons
        ttk.Button(self, text='OK', default='active', command=self.click_ok).pack(side=tk.RIGHT)
        ttk.Button(self, text='Cancel', command=self.click_cancel).pack(side=tk.RIGHT)

        # blank option menu
        # self.master.config(menu=tk.Menu(self.master))

    def click_ok(self):
        print "Clicked ok"

    def click_cancel(self):
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()
