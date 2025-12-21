import tkinter as tk

def tinh_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        
        lbl_bmi_val.config(text=f"BMI: {bmi:.2f}")
        
        if bmi < 18.5: res = "Gầy"
        elif 18.5 <= bmi < 24.9: res = "Bình thường"
        elif 25 <= bmi < 29.9: res = "Tiền béo phì"
        else: res = "Béo phì"
        
        lbl_result.config(text=f"Kết luận: {res}")
    except ValueError:
        lbl_result.config(text="Lỗi: Nhập sai số liệu!")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

tk.Label(root, text="Cân nặng (kg):").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Chiều cao (m):").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack()

tk.Button(root, text="Tính BMI", command=tinh_bmi).pack(pady=10)

lbl_bmi_val = tk.Label(root, text="BMI: --")
lbl_bmi_val.pack()

lbl_result = tk.Label(root, text="Kết luận: --", font=("Arial", 10, "bold"))
lbl_result.pack(pady=5)

root.mainloop()