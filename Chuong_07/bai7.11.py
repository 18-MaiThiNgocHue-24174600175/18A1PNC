import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def tinh_am_lich():
    try:
        nam_duong = int(entry_nam.get())
        if nam_duong < 0: raise ValueError
        
        can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
        chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
        
        ten_can = can[nam_duong % 10]
        ten_chi = chi[nam_duong % 12]
        nam_am = f"{ten_can} {ten_chi}"
        
        messagebox.showinfo("Kết quả", f"Năm Dương lịch {nam_duong} là năm: {nam_am}")
        
        hien_thi_con_giap(ten_chi)
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập năm là một số nguyên dương!")

def hien_thi_con_giap(ten_chi):
    try:
        path = f"D:/Chương7/18A1PNC/Chuong_07/Tý.png" 
        img = Image.open(path)
        img = img.resize((150, 150))
        photo = ImageTk.PhotoImage(img)
        lbl_img.config(image=photo)
        lbl_img.image = photo
    except:
        lbl_img.config(text=f"(Chưa có ảnh cho tuổi {ten_chi})", image='')

root = tk.Tk()
root.title("Bài 7.11: Đổi năm Dương lịch sang Âm lịch")
root.geometry("400x400")

tk.Label(root, text="Nhập năm Dương lịch:", font=("Arial", 12)).pack(pady=10)
entry_nam = tk.Entry(root, font=("Arial", 12), justify='center')
entry_nam.pack(pady=5)

btn_convert = tk.Button(root, text="Chuyển đổi", command=tinh_am_lich, bg="orange", fg="white", font=("Arial", 10, "bold"))
btn_convert.pack(pady=20)

lbl_img = tk.Label(root)
lbl_img.pack(pady=10)

root.mainloop()