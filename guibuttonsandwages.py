import tkinter as tk
root = tk.Tk()
def show():
    label2.config(text=entry.get())
label1 = tk.Label(root, text="Enter Name:")
label1.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Submit", command=show)
button.pack()
label2 = tk.Label(root, text="")
label2.pack()
root.mainloop()


