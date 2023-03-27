"""
import numpy
import random

#print(dir(random))
print(help(random.choice))

import os, sys
print(os.getcwd()) #현재 디렉토리 표시
print('\n')
print(sys.path) #환경변수에 지정된 디렉토리

import os

# 현재 작업 디렉토리 확인
current_dir = os.getcwd()
print("현재 작업 디렉토리:", current_dir)

# 새로운 디렉토리 생성
new_dir = "new_directory"
os.mkdir(new_dir)
print(f"새로운 디렉토리 '{new_dir}'가 생성되었습니다.")

# 생성한 디렉토리 내에 파일 생성
new_file = "new_file.txt"
with open(os.path.join(new_dir, new_file), "w") as f:
    f.write("새로운 파일 내용")
print(f"'{new_file}' 파일이 '{new_dir}' 디렉토리 내에 생성되었습니다.")

# 지정된 디렉토리의 파일 및 디렉토리 목록 확인
list_dir = os.listdir(new_dir)
print(f"'{new_dir}' 디렉토리 내의 파일 및 디렉토리 목록: {list_dir}")

# 파일인지 디렉토리인지 확인
for item in list_dir:
    item_path = os.path.join(new_dir, item)
    if os.path.isfile(item_path):
        print(f"'{item_path}'는 파일입니다.")
    elif os.path.isdir(item_path):
        print(f"'{item_path}'는 디렉토리입니다.")

# 파일 삭제
os.remove(os.path.join(new_dir, new_file))
print(f"'{new_file}' 파일이 삭제되었습니다.")

# 디렉토리 삭제
os.rmdir(new_dir)
print(f"'{new_dir}' 디렉토리가 삭제되었습니다.")
"""

import datetime

# 현재 날짜
today = datetime.date.today()

# 100일 후의 날짜
hundred_days_later = today + datetime.timedelta(days=100)

# 1000일 후의 날짜
thousand_days_later = today + datetime.timedelta(days=1000)

# 결과 출력
print("100일 후:", hundred_days_later)
print("1000일 후:", thousand_days_later)



import calendar

# 2023년 3월의 달력을 출력합니다.
print("2023년 3월의 달력:")
print(calendar.month(2023, 3))

# 2023년 3월 15일의 요일을 확인합니다. (월요일: 0, 화요일: 1, ..., 일요일: 6)
year = 2023
month = 3
day = 15
weekday = calendar.weekday(year, month, day)
print("2023년 3월 15일은 요일 인덱스 {}에 해당하는 요일입니다.".format(weekday))

# 요일 인덱스를 사용하여 요일 이름을 가져옵니다.
weekday_name = calendar.day_name[weekday]
print("2023년 3월 15일은 {}입니다.".format(weekday_name))




import pandas as pd

# 시리즈(Series) 예시
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)

# 데이터프레임(DataFrame) 예시
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'year': [2017, 2017, 2018, 2019],
        'score': [100, 95, 80, 90]}
df = pd.DataFrame(data)
print(df)

# 데이터프레임에서 열 선택 예시
print(df['name'])
print(df.year)

# 조건을 이용한 데이터 선택 예시
print(df[df.year > 2017])

# 데이터프레임에 열 추가 예시
df['grade'] = ['A', 'A-', 'B+', 'B']
print(df)

# 데이터프레임에서 행 선택 예시
print(df.loc[0])
print(df.loc[[0, 2]])

# 데이터프레임에서 행과 열 선택 예시
print(df.loc[0, 'name'])
print(df.loc[[0, 2], ['name', 'score']])

import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(-np.pi, np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 그래프 그리기
plt.plot(x, y_sin, label='sin')
plt.plot(x, y_cos, label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sin and Cos Functions')
plt.legend()
plt.show()

