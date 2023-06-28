import os
import tkinter as tk
from tkinter import messagebox

def find_file(start_path, file_name):
    for dirpath, dirnames, filenames in os.walk(start_path):
        if file_name in filenames:
            return os.path.join(dirpath, file_name)
    return None

def search():
    file_name = entry.get()
    file_path = find_file('C:/', file_name)

    if file_path:
        messagebox.showinfo("결과", f"파일 위치: {file_path}")
    else:
        messagebox.showinfo("결과", "파일을 찾을 수 없습니다.")

root = tk.Tk()
root.geometry("500x500+500+500")

label = tk.Label(root, text="파일 이름 입력:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="검색", command=search)
button.pack()

root.mainloop()
