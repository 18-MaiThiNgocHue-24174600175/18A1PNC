import tkinter as tk
from tkinter import messagebox

def show_info(menu_item):
    if menu_item == "1.1":
        messagebox.showinfo("Lập trình hướng đối tượng", "Giải phương trình bậc 2")

root = tk.Tk()
root.title("Hệ thống bài tập nâng cao Python")
root.geometry("500x300")

menubar = tk.Menu(root)

chuong1 = tk.Menu(menubar, tearoff=0)
chuong1.add_command(label="1.1", command=lambda: show_info("1.1"))
chuong1.add_command(label="1.2")
chuong1.add_separator()
chuong1.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="Chương 1", menu=chuong1)

menubar.add_cascade(label="Chương 2", menu=tk.Menu(menubar, tearoff=0))
menubar.add_cascade(label="Chương 3", menu=tk.Menu(menubar, tearoff=0))
menubar.add_cascade(label="Chương 4", menu=tk.Menu(menubar, tearoff=0))

root.config(menu=menubar)
root.mainloop()