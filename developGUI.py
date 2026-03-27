import tkinter as tk
root = tk.Tk()
root.title("CheckButton and Radiobutton")
var1 = tk.IntVar()
var2 = tk.IntVar()
tk.Checkbutton(root, text="Option 1", variable=var1).pack()
tk.Checkbutton(root, text="Option 2", variable=var2).pack()
var = tk.IntVar()
tk.Radiobutton(root, text="Male", variable=var, value=1).pack()
tk.Radiobutton(root, text="Female", variable=var, value=2).pack()
root.mainloop()


