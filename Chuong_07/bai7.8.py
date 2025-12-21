import tkinter as tk

def liet_ke_uoc():
    try:
        n = int(entry_n.get())
        uoc_so = [str(i) for i in range(1, n + 1) if n % i == 0]
        lbl_result.config(text=f"The divisors of N: {' '.join(uoc_so)}")
    except ValueError:
        lbl_result.config(text="Vui lòng nhập số nguyên!")

root = tk.Tk()
root.title("tk")
root.geometry("400x200")

tk.Label(root, text="Enter the value of N:").place(x=50, y=50)
entry_n = tk.Entry(root)
entry_n.place(x=180, y=50)

lbl_result = tk.Label(root, text="The divisors of N: ")
lbl_result.place(x=50, y=90)

tk.Button(root, text="Validate", command=liet_ke_uoc).place(x=180, y=130)

root.mainloop()