import os
import tkinter as tk
from tkinter import filedialog, ttk
from filter import filter

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        source_var.set(folder)
        keyword_var.set(folder.split("/")[-1])



def list_files():
    folder = source_var.get()
    extention= extention_var.get()
    if not folder or not extention:
        result_var.set("Please select folder and extention")
        return

    files = [f for f in os.listdir(folder) if keyword_var.get().lower() in f.lower() and f.endswith(extention.lower())]
    result_var.set(f"Found {len(files)} files with '{extention} extention") 
    filter(keyword_var.get(),source_var.get(),extention_var.get())

root = tk.Tk()
root.title("Nvidia Clip Filter")

source_var = tk.StringVar()
keyword_var = tk.StringVar()
extention_var = tk.StringVar()
result_var = tk.StringVar()



tk.Label(root,text="Source Folder").grid(row=0,column=0)
tk.Entry(root, textvariable=source_var,width=40).grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_folder).grid(row=0,column=2)

tk.Label(root, text="Select Extention").grid(row=2,column=0)
ttk.Combobox(root,textvariable=extention_var, values=[".mp4",".mov"]).grid(row=2,column=1)
extention_var.set(".mp4")
tk.Button(root, text="List Files", command=list_files).grid(row=3, column=1)

tk.Label(root,textvariable=result_var, fg="red").grid(row=4,column=0)



root.mainloop()