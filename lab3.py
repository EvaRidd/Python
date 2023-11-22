import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox

def generate_key(hex):
    try:
        dec = int(hex, 16)
        key_3 = str(dec)[:3]
        key_2 = str(dec)[-2:]
        generated_key = f"{key_3}-{key_2}"
        key.set(generated_key)
    except ValueError:
        key.set("Error")
        tk.messagebox.showwarning('Error')

def close():
    window.destroy()


window = tk.Tk()
window.title("HEX TO DEC :)")


background_image = PhotoImage(file="t.png")


window.geometry('576x360')

lbl_bg = tk.Label(window, image=background_image)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=0.5)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')


input_label = tk.Label(frame, text="Введите число в HEX:")
input_label.pack(pady=10)
hex_input_entry = tk.Entry(frame)
hex_input_entry.pack(pady=10, padx=10)


key = tk.StringVar()


key_label = tk.Label(frame, textvariable=key)
key_label.pack(pady=10, padx=10)


generate_button = tk.Button(frame, text="Calculate", command=lambda: generate_key(hex_input_entry.get()))
generate_button.pack(pady=10)
btn_exit = tk.Button(frame, text='Cancel', command=close)
btn_exit.pack(pady=15)


window.mainloop()