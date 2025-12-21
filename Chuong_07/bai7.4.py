import tkinter as tk

def gui_thong_tin():
    print("Thông tin đã được gửi!")

root = tk.Tk()
root.title("Bài 7.4: Form thông tin sinh viên")

# Nhãn và ô nhập Tên
tk.Label(root, text="Tên sinh viên:").grid(row=0, column=0, padx=10, pady=5)
entry_ten = tk.Entry(root)
entry_ten.grid(row=0, column=1, padx=10, pady=5)

# Nhãn và ô nhập ID
tk.Label(root, text="ID sinh viên:").grid(row=1, column=0, padx=10, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=1, column=1, padx=10, pady=5)

# Nhãn và ô nhập Mật khẩu (ẩn ký tự)
tk.Label(root, text="Mật khẩu:").grid(row=2, column=0, padx=10, pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.grid(row=2, column=1, padx=10, pady=5)

btn_gui = tk.Button(root, text="Gửi", command=gui_thong_tin)
btn_gui.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()