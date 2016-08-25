import Tkinter as tk
import ttk
import tkMessageBox

root = tk.Tk()
root.style = ttk.Style()
root.style.theme_use('clam')

def get_sum():
    global num1, num2, result
    try:
        n1 = int(num1.get())
        n2 = int(num2.get())
        result.delete(0, tk.END)
        result.insert(0, str(n1 + n2))
    except:
        tkMessageBox.showerror('Error', 'Debe ingresar valores')
        num1.focus()

calc_frame = tk.Frame(root)
calc_frame.pack()

num1 = ttk.Entry(calc_frame)
num1.pack(side=tk.LEFT)

ttk.Label(calc_frame, text='+').pack(side=tk.LEFT)

num2 = ttk.Entry(calc_frame)
num2.pack(side=tk.LEFT)

equal_btn = ttk.Button(calc_frame, text='=', command=get_sum)
equal_btn.pack(side=tk.LEFT)

result = ttk.Entry(calc_frame)
result.pack(side=tk.LEFT)
root.mainloop()
