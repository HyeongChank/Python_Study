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
    file_name_part1 = entry1.get()
    file_paths = find_files('C:/', file_name_part1)

    file_name_part2 = entry2.get()
    filtered_file_paths = [path for path in file_paths if file_name_part2 in os.path.basename(path)]

    # Text 위젯의 내용을 지웁니다.
    text.delete(1.0, tk.END)

    if filtered_file_paths:
        result_message = "\n".join(filtered_file_paths)
        text.insert(tk.END, f"파일 위치\n{result_message}")
    else:
        text.insert(tk.END, "파일을 찾을 수 없습니다.")

root = tk.Tk()
root.title("-HC- 파일 검색 프로그램")
description_text = "-HC- 파일 검색 프로그램\n\n"
description_text += "이 응용 프로그램은 파일 검색을 위한 도구입니다.\n"
description_text += "찾으려는 경로의 파일명을 입력 후 검색을 누르십시오.\n"
description_text += "파일명의 일부분을 입력하시면 해당 텍스트를 포함하고 있는 파일 전체가 검색됩니다.\n"
description_text += "**검색 범위를 좁히려면 두번째 입력란에 파일명의 일부분(첫번째와 다른) 추가 작성**"

description_label = tk.Label(root, text=description_text)
description_label.pack()

frame = tk.Frame(root, height=10)
frame.pack()

label1 = tk.Label(root, text="파일 이름(일부 작성 가능)")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="파일 이름(추가 입력 필요 시)")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

button = tk.Button(root, text="검색", command=search)
button.pack()

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Text 위젯의 크기를 설정합니다.
text = tk.Text(root, wrap=tk.NONE, yscrollcommand=scrollbar.set, width=130, height=50)
text.pack()

scrollbar.config(command=text.yview)

root.mainloop()
