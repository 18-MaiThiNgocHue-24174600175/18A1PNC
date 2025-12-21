import tkinter as tk

def tinh_tien():
    try:
        km = float(entry_km.get())
        wait_time = int(entry_wait.get())
        car_type = var_car.get()
        
        tien_cho = max(0, wait_time - 5) * 750
        
        if car_type == 4:
            if km <= 0.8: total = 12000
            elif km <= 30: total = 12000 + (km - 0.8) * 15300
            else: total = 12000 + (30 - 0.8) * 15300 + (km - 30) * 12100
        else: 
            if km <= 0.8: total = 12000
            elif km <= 30: total = 12000 + (km - 0.8) * 16100
            else: total = 12000 + (30 - 0.8) * 16100 + (km - 30) * 13800
            
        lbl_total.config(text=f"Tổng tiền: {int(total + tien_cho):,} đồng")
    except ValueError:
        lbl_total.config(text="Vui lòng nhập số hợp lệ!")

root = tk.Tk()
root.title("Tính cước Taxi")

tk.Label(root, text="Nhập số km:").pack()
entry_km = tk.Entry(root)
entry_km.pack()

tk.Label(root, text="Thời gian chờ (phút):").pack()
entry_wait = tk.Entry(root)
entry_wait.pack()

var_car = tk.IntVar(value=4)
tk.Radiobutton(root, text="Xe 4 chỗ", variable=var_car, value=4).pack()
tk.Radiobutton(root, text="Xe 7 chỗ", variable=var_car, value=7).pack()

tk.Button(root, text="Tính tiền", command=tinh_tien).pack(pady=10)
lbl_total = tk.Label(root, text="Tổng tiền: 0 đồng", font=("Arial", 11, "bold"))
lbl_total.pack()

root.mainloop()