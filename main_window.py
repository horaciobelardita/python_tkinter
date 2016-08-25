import Tkinter as tk
import ttk

root = tk.Tk()

ttk.Label(root, text='Hello').pack(side=tk.TOP)
ttk.Label(root, text='Goodbye').pack(side=tk.BOTTOM)

btn = ttk.Button(root, text="First Button")
btn.pack()




root.mainloop()
