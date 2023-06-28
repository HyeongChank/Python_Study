import os

# C 드라이브의 'user' 디렉토리 경로를 생성합니다.
directory = 'C:/user'
directory2 = 'c:'
# 생성할 폴더의 경로를 생성합니다.
folder = os.path.join(directory, 'test')
folder2 = os.path.join(directory2, 'test2')

# 해당 경로에 폴더가 없다면 폴더를 생성합니다.
if not os.path.exists(folder):
    os.makedirs(folder)
else:
    os.makedirs(folder2)
