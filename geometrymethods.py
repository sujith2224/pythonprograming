import tkinter as tk
root = tk.Tk()
frame1 = tk.Frame(root)
frame1.pack()
frame2 = tk.Frame(root)
frame2.pack()
label1 = tk.Label(frame1, text="Using Pack")
label1.pack()
label2 = tk.Label(frame2, text="Using Grid")
label2.grid(row=0, column=0)
label3 = tk.Label(root, text="Using Place")
label3.place(x=50, y=50)
root.mainloop()



