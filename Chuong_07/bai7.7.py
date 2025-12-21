import tkinter as tk

def tinh_tong():
    try:
        n = int(entry_n.get())
        if n < 0:
            lbl_tong.config(text="Vui lòng nhập số dương")
            return
        
        tong = sum(range(1, n + 1))
        lbl_tong.config(text=f"Tổng 1 + 2 + ... + {n} là: {tong}")
    except ValueError:
        lbl_tong.config(text="Lỗi: Hãy nhập một số nguyên!")

root = tk.Tk()
root.title("Tính tổng số nguyên")
root.geometry("350x200")

tk.Label(root, text="Nhập số nguyên N:").pack(pady=10)
entry_n = tk.Entry(root)
entry_n.pack(pady=5)

btn_tinh = tk.Button(root, text="Tính Tổng", command=tinh_tong)
btn_tinh.pack(pady=10)

lbl_tong = tk.Label(root, text="Kết quả sẽ hiển thị ở đây", font=("Arial", 10, "bold"))
lbl_tong.pack(pady=10)

root.mainloop()