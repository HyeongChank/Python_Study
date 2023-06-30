import os
import shutil

def delete_folder(start_path, folder_name):
    for dirpath, dirnames, filenames in os.walk(start_path):
        if os.path.basename(dirpath) == folder_name:
            # 해당 폴더를 찾으면 삭제합니다.
            shutil.rmtree(dirpath)
            print(f"The folder {dirpath} has been successfully deleted.")
            return

    print(f"Folder named {folder_name} not found in {start_path}.")

# 사용 예:
# C 드라이브에서 'test2'라는 이름의 폴더를 삭제합니다.
delete_folder('C:/', 'test2')
