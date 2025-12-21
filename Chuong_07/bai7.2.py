import tkinter as tk

root = tk.Tk()
root.title("Bài 7.2: Thêm nhãn")

# Tạo một nhãn 
label = tk.Label(root, text="Chào mừng bạn đến với Tkinter!")

# Hiển thị nhãn lên cửa sổ
label.pack()

root.mainloop()