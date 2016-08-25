import Tkinter as tk
import ttk

root = tk.Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
names_frame = tk.Frame(root)
names_frame.grid(row=0)

ttk.Label(names_frame, text='First name').grid(row=0, sticky=tk.W, padx=10)
ttk.Entry(names_frame).grid(row=0, column=1, sticky=tk.E, pady=10)

ttk.Label(names_frame, text='Last name').grid(row=1, sticky=tk.W, padx=10)
ttk.Entry(names_frame).grid(row=1, column=1, sticky=tk.E, pady=10)

ttk.Button(names_frame, text='Submit').grid(row=2, columnspan=2)

frame = tk.Frame(root)
frame.grid(row=1)
ttk.Label(frame)

ttk.Label(frame, text='Description').grid(row=0, column=0)
ttk.Entry(frame, width=50).grid(row=0, column=1)
ttk.Button(frame, text='Submit').grid(row=0, column=8)

ttk.Label(frame, text='Quality').grid(row=1, column=0)
ttk.Radiobutton(frame, text='New', value=1).grid(row=2, column=0)
ttk.Radiobutton(frame, text='Good', value=2).grid(row=3, column=0)
ttk.Radiobutton(frame, text='Poor', value=3).grid(row=4, column=0)

ttk.Label(frame, text='Benefits').grid(row=1, column=1)
ttk.Checkbutton(frame, text='Free shipping').grid(row=2, column=1)

root.mainloop()
