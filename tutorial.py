import Tkinter as tk
import ttk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()
label_text = tk.StringVar()

ttk.Label(frame, textvariable=label_text).pack()
ttk.Button(frame, text='Click me!!').pack()
label_text.set('I am a label')
root.mainloop()
