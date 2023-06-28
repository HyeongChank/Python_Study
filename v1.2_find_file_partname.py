import os
import tkinter as tk
from tkinter import messagebox

def find_files(start_path, file_name_part):
    result = []
    for dirpath, dirnames, filenames in os.walk(start_path):
        for filename in filenames:
            if file_name_part in filename:
                result.append(os.path.join(dirpath, filename))
    return result

def search():
    file_name_part = entry.get()
    file_paths = find_files('C:/', file_name_part)

    if file_paths:
        result_message = "\n".join(file_paths)
        messagebox.showinfo("결과", f"파일 위치: {result_message}")
    else:
        messagebox.showinfo("결과", "파일을 찾을 수 없습니다.")

root = tk.Tk()
root.geometry("500x500+500+500")
label = tk.Label(root, text="파일 이름 일부 입력:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="검색", command=search)
button.pack()

root.mainloop()
