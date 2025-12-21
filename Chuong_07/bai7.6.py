import tkinter as tk

def dao_nguoc_chuoi():
    input_str = entry_word.get()
    reversed_str = ""
    for i in range(len(input_str) - 1, -1, -1):
        reversed_str += input_str[i]
    
    lbl_result.config(text=reversed_str)

root = tk.Tk()
root.title("tk")
root.geometry("400x200")

tk.Label(root, text="Enter a word:").place(x=50, y=50)
entry_word = tk.Entry(root)
entry_word.place(x=150, y=50, width=150)

lbl_result = tk.Label(root, text="", fg="black")
lbl_result.place(x=150, y=80)

btn_validate = tk.Button(root, text="Validate", command=dao_nguoc_chuoi)
btn_validate.place(x=150, y=120, width=100)

root.mainloop()