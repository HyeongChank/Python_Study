import os
import tkinter as tk

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

    # Text 위젯의 내용을 지웁니다.
    text.delete(1.0, tk.END)

    if file_paths:
        result_message = "\n".join(file_paths)
        text.insert(tk.END, f"파일 위치: {result_message}")
    else:
        text.insert(tk.END, "파일을 찾을 수 없습니다.")

root = tk.Tk()
root.geometry("1000x1000+500+500")
label = tk.Label(root, text="파일 이름 일부 입력:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="검색", command=search)
button.pack()

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text = tk.Text(root, wrap=tk.NONE, yscrollcommand=scrollbar.set, width=100, height=50)
text.pack()

scrollbar.config(command=text.yview)

root.mainloop()
