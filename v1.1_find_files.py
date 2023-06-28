import os
import tkinter as tk
from tkinter import messagebox

def find_files(start_path, file_name):
    result = []
    for dirpath, dirnames, filenames in os.walk(start_path):
        if file_name in filenames:
            result.append(os.path.join(dirpath, file_name))
    return result

def search():
    file_name = entry.get()
    file_paths = find_files('C:/', file_name)

    if file_paths:
        result_message = "\n".join(file_paths)
        messagebox.showinfo("결과", f"파일 위치: {result_message}")
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
