import tkinter as tk

root = tk.Tk()
root.title("Bài 7.3: Tùy chỉnh Font")

label = tk.Label(
    root, 
    text="Dòng chữ này đã thay đổi font", 
    font=("Arial", 16, "bold")
)

label.pack(padx=20, pady=20)

root.mainloop()