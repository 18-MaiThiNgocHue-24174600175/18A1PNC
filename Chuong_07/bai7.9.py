import tkinter as tk
from tkinter import ttk
import math

def calculate():
    try:
        m = int(entry_m.get())
        n = int(entry_n.get())
        func = combo.get()
        
        if func == "GCD":
            res = math.gcd(m, n)
            lbl_res.config(text=f"GCD(m, n) = {res}")
        else:
            res = abs(m * n) // math.gcd(m, n)
            lbl_res.config(text=f"LCM(m, n) = {res}")
    except:
        lbl_res.config(text="Lỗi nhập liệu!")

root = tk.Tk()
root.title("GCD & LCM")
root.geometry("350x250")

tk.Label(root, text="Enter value of m:").grid(row=0, column=0, padx=10, pady=10)
entry_m = tk.Entry(root)
entry_m.grid(row=0, column=1)

tk.Label(root, text="Enter value of n:").grid(row=1, column=0, padx=10, pady=10)
entry_n = tk.Entry(root)
entry_n.grid(row=1, column=1)

tk.Label(root, text="Choose function:").grid(row=2, column=0, padx=10, pady=10)
combo = ttk.Combobox(root, values=["GCD", "LCM"])
combo.current(0)
combo.grid(row=2, column=1)

lbl_res = tk.Label(root, text="Kết quả")
lbl_res.grid(row=3, column=0, columnspan=2, pady=10)

tk.Button(root, text="Calculate", command=calculate).grid(row=4, column=0, columnspan=2)

root.mainloop()