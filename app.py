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
root.configure(bg="#f2f2f2")

title = tk.Label(root,
                 text="Simple Interest Calculator",
                 font=("Arial",16,"bold"),
                 bg="#f2f2f2",
                 fg="#333333")
title.pack(pady=10)

tk.Label(root,text="Principal",bg="#f2f2f2", fg="#333333").pack()

principal = tk.Entry(root)
principal.pack()

tk.Label(root,text="Rate (%)",bg="#f2f2f2", fg="#333333").pack()

rate = tk.Entry(root)
rate.pack()

tk.Label(root,text="Time (Years)",bg="#f2f2f2", fg="#333333").pack()

time = tk.Entry(root)
time.pack()

tk.Button(root,
          text="Calculate",
          command=calculate,
          bg="#4CAF50",
          fg="white").pack(pady=15)

result = tk.Label(root,
                  text="",
                  font=("Arial",14),
                  bg="#f2f2f2",
                  fg="#333333")

result.pack()

root.mainloop()