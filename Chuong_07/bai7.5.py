import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os

def hien_thi_anh_local():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    img_path = os.path.join(dir_path, "Otto.png")
    
    try:
        img = Image.open(img_path)
        img = img.resize((400, 300))
        photo = ImageTk.PhotoImage(img)
        lbl_img.config(image=photo, text="") 
        lbl_img.image = photo
        print("Đã hiển thị ảnh local thành công!")
    except Exception as e:
        print(f"Lỗi ảnh local: {e}")
        lbl_img.config(text=f"Không tìm thấy file: {img_path}")

def tai_anh_tu_url():
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/American_Eskimo_Dog.jpg/640px-American_Eskimo_Dog.jpg"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img = img.resize((400, 300))
        
        photo = ImageTk.PhotoImage(img)
        lbl_img.config(image=photo, text="")
        lbl_img.image = photo
        print("Tải ảnh từ URL thành công!")
    except Exception as e:
        print(f"Lỗi URL: {e}")
        lbl_img.config(text="Không thể tải ảnh từ URL này")
root = tk.Tk()
root.title("Chương trình xem ảnh - Bài 7.5")
root.geometry("500x450")

lbl_img = tk.Label(root, text="Chưa có ảnh hiển thị", font=("Arial", 12))
lbl_img.pack(pady=20, expand=True)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

btn_local = tk.Button(btn_frame, text="Xem ảnh Local", command=hien_thi_anh_local, width=15)
btn_local.grid(row=0, column=0, padx=10)

btn_url = tk.Button(btn_frame, text="Tải ảnh URL", command=tai_anh_tu_url, width=15, bg="lightblue")
btn_url.grid(row=0, column=1, padx=10)

root.mainloop()