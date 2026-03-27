import tkinter as tk
from tkinter import messagebox, filedialog
root = tk.Tk()
root.title("Advanced GUI")
frame = tk.Frame(root)
frame.pack()
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
for item in ["Python", "Java", "C++", "HTML", "CSS"]:
    listbox.insert(tk.END, item)
listbox.pack()
scrollbar.config(command=listbox.yview)
def show_msg():
    messagebox.showinfo("Message", "Hello User!")
def open_file():
    filedialog.askopenfilename()
tk.Button(root, text="Show Message", command=show_msg).pack()
tk.Button(root, text="Open File", command=open_file).pack()
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Exit", command=root.quit)
mb = tk.Menubutton(root, text="Options", relief=tk.RAISED)
mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mb.menu.add_command(label="Option 1")
mb.menu.add_command(label="Option 2")
mb.pack()
root.mainloop()

