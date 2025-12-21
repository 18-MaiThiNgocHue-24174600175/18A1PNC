import tkinter as tk
from tkinter import messagebox

def check_age():
    ten = entry_ten.get()
    try:
        tuoi = int(entry_tuoi.get())
        msg = f"Xin chào {ten}!\n"
        if tuoi >= 18:
            msg += "Bạn đã trưởng thành!"
        else:
            msg += "Bạn còn nhỏ tuổi!"
        messagebox.showinfo("Thông báo", msg)
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng số tuổi")

root = tk.Tk()
root.title("Kiểm tra tuổi")
root.geometry("300x150")

tk.Label(root, text="Tên:").pack()
entry_ten = tk.Entry(root)
entry_ten.pack()

tk.Label(root, text="Tuổi:").pack()
entry_tuoi = tk.Entry(root)
entry_tuoi.pack()

tk.Button(root, text="Kiểm tra", command=check_age).pack(pady=10)

root.mainloop()