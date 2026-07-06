import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        p = float(principal.get())
        r = float(rate.get())
        n = float(time.get())

        si = (p * r * n) / 100

        result.config(text=f"Simple Interest = {si:.2f}")

    except:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("400x350")
root.configure(bg="#d9f2ff")

title = tk.Label(root,
                 text="Simple Interest Calculator",
                 font=("Arial",16,"bold"),
                 bg="#d9f2ff")
title.pack(pady=10)

tk.Label(root,text="Principal",bg="#d9f2ff").pack()

principal = tk.Entry(root)
principal.pack()

tk.Label(root,text="Rate (%)",bg="#d9f2ff").pack()

rate = tk.Entry(root)
rate.pack()

tk.Label(root,text="Time (Years)",bg="#d9f2ff").pack()

time = tk.Entry(root)
time.pack()

tk.Button(root,
          text="Calculate",
          command=calculate,
          bg="blue",
          fg="white").pack(pady=15)

result = tk.Label(root,
                  text="",
                  font=("Arial",14),
                  bg="#d9f2ff")

result.pack()

root.mainloop()