import numpy as np
"""
# 1차원 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # [1 2 3 4 5]

# 2차원 배열 생성
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

# 배열 데이터 타입 지정
arr3 = np.array([1, 2, 3], dtype=float)
print(arr3)  # [1. 2. 3.]

# 3차원 배열 생성
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d)

# 4차원 배열 생성
arr4d = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
print(arr4d)

arr = np.array([1, 2, 3, 4, 5])

# 인덱스가 0부터 시작하므로 arr[0]은 첫번째 요소를 의미함
print(arr[0])  # 1

# 음수 인덱스를 사용하면 배열의 끝부터 요소를 선택할 수 있음
print(arr[-1])  # 5

# 다차원 배열의 인덱싱
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 0])  # 1
print(arr2d[1, 1])  # 5

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6, 7])

# 브로드캐스팅을 통해 크기가 다른 배열 간 연산이 가능
print(arr1 + arr2)  # [ 5  7  9 10]


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# 배열 형태 변경
arr2d = arr.reshape((2, 4))
print(arr2d)

# 배열 구조 변경
arr2d_reshape = arr2d.reshape(4, 2)
print(arr2d_reshape)

# 배열 전치(Transpose)
arr2d_transpose = arr2d.T
print(arr2d_transpose)



# 정규 분포
arr1 = np.random.normal(0, 1, size=10)
print(arr1)
'''
[-1.03175853 -0.26330108  0.50114289  0.43128428  1.52632134
 -0.11669154 -0.38778772 -0.58322862  0.1852227  -1.12919514]
'''

# 균등 분포
arr2 = np.random.uniform(0, 1, size=10)
print(arr2)
'''
[0.3082703  0.59827088 0.61679035 0.3049514  0.10465949
 0.95647913 0.52484807 0.62345654 0.36863133 0.66491068]
'''

# 이항 분포
arr3 = np.random.binomial(10, 0.5, size=10)
print(arr3)
'''
[6 7 6 3 7 3 6 3 7 3]
'''

# 포아송 분포
arr4 = np.random.poisson(3, size=10)
print(arr4)
'''
[2 2 2 6 2 1 1 1 1 6]
'''

#======================================================================

import pandas as pd

# Series 생성
# 리스트 사용
data = pd.Series([1, 2, 3, 4])
print(data)
# 결과:
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64


# 문자열 인덱스 사용
data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(data)

# 딕셔너리 사용
data1 = {'a': 1, 'b': 2, 'c': 3 , 'd': 4}
s1 = pd.Series(data1)
print(s1)

# 결과:
# a    1
# b    2
# c    3
# d    4
# dtype: int64

# 시리즈 생성
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)

# 시리즈 인덱싱
print(s['a'])  # 10
print(s[['a', 'c', 'e']])  # a    10, c    30, e    50
print(s[:3])  # a    10, b    20, c    30
print(s[s > 30])  # d    40, e    50



import pandas as pd

# 시리즈 생성
data1 = {'a': 1, 'b': 2, 'c': 3}
data2 = {'a': 10, 'c': 30, 'd': 40}
s1 = pd.Series(data1)
s2 = pd.Series(data2)

# 덧셈 연산
s = s1 + s2
print(s)  # a    11.0, b     NaN, c    33.0, d     NaN
           # dtype: float64

# 뺄셈 연산
s = s1 - s2
print(s)  # a    -9.0, b     NaN, c   -27.0, d     NaN
           # dtype: float64

# 곱셈 연산
s = s1 * s2
print(s)  # a    10.0, b     NaN, c    90.0, d     NaN
           # dtype: float64

# 나눗셈 연산
s = s1 / s2
print(s)  # a    0.1 , b     NaN, c    0.1 , d     NaN
           # dtype: float64


import pandas as pd

# 시리즈 생성
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)

# 집계 함수 예시
print(s.sum())  # 150
print(s.mean())  # 30.0
print(s.std())  # 15.811388300841896
print(s.max())  # 50
print(s.min())  # 10



import pandas as pd
import numpy as np

# 데이터프레임 생성 방법 1: 딕셔너리를 이용한 데이터프레임 생성
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print(df1)

# 데이터프레임 생성 방법 2: 리스트를 이용한 데이터프레임 생성
data = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
df2 = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df2)

# 데이터프레임 생성 방법 3: Numpy 배열을 이용한 데이터프레임 생성
arr = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
df3 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df3)

# 데이터프레임 생성 방법 4: 시리즈를 이용한 데이터프레임 생성
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
s3 = pd.Series([7, 8, 9])
df4 = pd.DataFrame({'A': s1, 'B': s2, 'C': s3})
print(df4)


import pandas as pd
import numpy as np
# # 데이터프레임 생성 방법 5: 외부 데이터 파일을 이용한 데이터프레임 생성
df5 = pd.read_csv('data.csv')
print(df5)


import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva','khc'],
        'age': [25, 30, 35, 40, 45,33],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo', 'seoul']}
df = pd.DataFrame(data)

# 데이터프레임 정보 출력
print(df.head())            # 상위 5개 데이터 출력
print(df.tail())            # 하위 5개 데이터 출력
print(df.info())            # 데이터프레임 정보 출력
print('\n', "기술 통계 출력")
print(df.describe())        # 수치형 열의 기술 통계 정보 출력
print(df.columns)           # 열 이름 출력
print(df.index)             # 행 인덱스 출력
print('\n')
print("datatype " , df.dtypes)            # 열의 데이터 타입 출력
print("datashape ", df.shape)             # 데이터프레임의 크기 출력
print(df.isnull().sum())    # 결측치 개수 출력



import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 열 선택 방법 1: 대괄호([])를 이용한 단일 열 선택
name_col = df['name']
print(name_col)

# 열 선택 방법 2: 점(.)을 이용한 단일 열 선택
age_col = df.age
print(age_col)

# 열 선택 방법 3: 대괄호([])를 이용한 복수 열 선택
name_age_col = df[['name', 'age']]
print(name_age_col)

# 열 선택 방법 4: loc[]를 이용한 열 선택
name_col = df.loc[:, 'name']
print(name_col)

# 열 선택 방법 5: iloc[]를 이용한 열 선택
name_age_col = df.iloc[:, [0, 1]]
print(name_age_col)


import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 열 선택 방법 1: 대괄호([])를 이용한 단일 열 선택
name_col = df['name']
print(name_col)

# 열 선택 방법 2: 점(.)을 이용한 단일 열 선택
age_col = df.age
print(age_col)

# 열 선택 방법 3: 대괄호([])를 이용한 복수 열 선택
name_age_col = df[['name', 'age']]
print(name_age_col)

# 열 선택 방법 4: loc[]를 이용한 열 선택
name_col = df.loc[:, 'name']
print(name_col)

# 열 선택 방법 5: iloc[]를 이용한 열 선택
name_age_col = df.iloc[:, [0, 1]]
print(name_age_col)


import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 부분 데이터 선택 방법 1: loc[]를 이용한 조건에 따른 선택
sub_df_1 = df.loc[df['age'] > 30, ['name', 'city']]
print(sub_df_1)

# 부분 데이터 선택 방법 2: query()를 이용한 조건에 따른 선택
sub_df_2 = df.query('age > 30')[['name', 'city']]
print(sub_df_2)

# 부분 데이터 선택 방법 3: 슬라이싱을 이용한 범위 지정
sub_df_3 = df.iloc[1:3, 1:3]
print(sub_df_3)

# 부분 데이터 선택 방법 4: iloc[]를 이용한 인덱스 지정
sub_df_4 = df.iloc[[1, 3], [0, 2]]
print(sub_df_4)

# 부분 데이터 선택 방법 5: 조건에 따른 선택 후 열 지정
sub_df_5 = df[df['age'] > 30][['name', 'city']]
print(sub_df_5)

# 부분 데이터 선택 방법 6: at[]을 이용한 특정 위치 선택
val = df.at[1, 'age']
print(val)





##데이터 전처리================================================

import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 열 추가 방법 1: 기존 열을 이용하여 새로운 열 추가
df['age2'] = df['age'] + 1

# 열 추가 방법 2: insert() 메소드를 이용하여 특정 위치에 열 추가
df.insert(loc=2, column='gender', value=['F', 'M', 'M', 'M', 'F'])

# 열 추가 방법 3: assign() 메소드를 이용하여 여러 개의 열 한 번에 추가
df = df.assign(age3=[26, 31, 36, 41, 46], height=[160, 170, 180, 175, 165])

# 출력
print(df)



import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 재정렬 방법 1: loc[]을 이용하여 행 순서 변경
df = df.loc[[4, 3, 2, 1, 0]]

# 행 재정렬 방법 2: sort_values() 메소드를 이용하여 열 기준으로 정렬
df = df.sort_values('age', ascending=False)

# 열 재정렬 방법 1: 열 이름 순서 변경
df = df[['city', 'name', 'age']]

# 열 재정렬 방법 2: 열 이름을 알파벳 순서로 정렬
df = df.reindex(sorted(df.columns), axis=1)

# 출력
print(df)


import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']})

result = pd.concat([df1, df2], axis=0, ignore_index=True)

print(result)



import pandas as pd
##merge
left = pd.DataFrame({'key': ['K0', 'K1', 'K3'],
                     'A': ['A0', 'A1', 'A3'],
                     'B': ['B0', 'B1', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K2', 'K3'],
                      'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']})

#inner가 default 임
result = pd.merge(left, right, on='key', how='inner')
print(result)

result = pd.merge(left, right, on='key', how='outer')
print(result)

result = pd.merge(left, right, on='key', how='left')
print(result)

result = pd.merge(left, right, on='key', how='right')
print(result)


import pandas as pd
##join

# 예시 데이터
left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']},
                     index=['K0', 'K1', 'K2', 'K3'])
right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                      index=['K0', 'K1', 'K2', 'K3'])

# 인덱스를 기준으로 병합
result = left.join(right)

print(result)



import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank'],
        'gender': ['F', 'M', 'M', 'M', 'F', 'M'],
        'age': [25, 30, 35, 40, 45, 50],
        'score1': [80, 70, 85, 75, 90, 95],
        'score2': [85, 75, 90, 80, 95, 100]}

df = pd.DataFrame(data)

# count
print(df.groupby('gender')[['score1', 'score2']].count())

# size
print(df.groupby('gender')[['score1', 'score2']].size())

# sum
print(df.groupby('gender')[['score1', 'score2']].sum())

# mean
print(df.groupby('gender')[['score1', 'score2']].mean())

# median
print(df.groupby('gender')[['score1', 'score2']].median())

# min
print(df.groupby('gender')[['score1', 'score2']].min())

# max
print(df.groupby('gender')[['score1', 'score2']].max())

# std
print(df.groupby('gender')[['score1', 'score2']].std())

# var
print(df.groupby('gender')[['score1', 'score2']].var())

# sem
print(df.groupby('gender')[['score1', 'score2']].sem())

# describe
print(df.groupby('gender')[['score1', 'score2']].describe())


import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
})

def my_func(x):
    return '-'.join(sorted(x))

result = df.groupby('A').agg({'B': my_func})

print(result)

#		          B
#A                         
#bar          one-three-two
#foo  one-one-three-two-two


import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob'],
    'Date': ['Day 1', 'Day 2', 'Day 1', 'Day 2', 'Day 1', 'Day 2', 'Day 1', 'Day 2'],
    'Date2': ['Day 1', 'Day 2', 'Day 1', 'Day 2', 'Day 1', 'Day 2', 'Day 1', 'Day 2'],
    'Value': [10, 20, 15, 25, 30, 40, 35, 45]
    
})

result = df.pivot_table(values='Value', index='Name', columns=['Date','Date2'], aggfunc='mean')

print(result)


import pandas as pd

# 나이 데이터 생성
ages = pd.DataFrame({'age': [22, 44, 65, 86, 27, 19, 51, 92, 33, 35, 38, 42, 14, 50, 78]})

# 연령대 구간 지정
bins = [0, 20, 40, 60, 80, 100]

# 연령대 카테고리 생성
age_categories = pd.cut(ages['age'], bins)

# 데이터프레임에 새로운 카테고리 열 추가
ages['age_categories'] = age_categories

# 결과 확인
print(ages)

result = pd.pivot_table(ages, index='age_categories', aggfunc='count')

print(result)




import pandas as pd

data = {'date': ['2021-08-15', '2021-08-16', '2021-08-17'],
        'value': [100, 200, 150]}
df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'])
print(df)
print(type(df['date']))
# Output:
#         date  value
# 0 2021-08-15    100
# 1 2021-08-16    200
# 2 2021-08-17    150

####자동으로 날짜로 인식하는 형식
%Y-%m-%d %H:%M:%S.%f
%Y-%m-%d %H:%M:%S
%Y-%m-%d %H:%M
%Y-%m-%d
%m/%d/%Y %H:%M:%S
%m/%d/%Y %H:%M
%m/%d/%Y
%m/%d/%y %H:%M:%S
%m/%d/%y %H:%M
%m/%d/%y


##위 형식이 아닐 때 to_datetime 써서 변경(아래 예제)
import pandas as pd

# 날짜 데이터 생성
df = pd.DataFrame({'date': ['2022년 01월 01일', '2022년 01월 02일', '2022년 01월 03일']})

# 날짜 데이터를 datetime 형식으로 변환
df['date'] = pd.to_datetime(df['date'], format='%Y년 %m월 %d일')

# 년, 월, 일 컬럼 추출
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

print(df)



import pandas as pd

data = {'date': ['2022-01-01', '2022-01-02', '2022-01-01', '2022-01-02', '2022-01-01', '2022-01-02', '2022-01-01', '2022-01-02', '2022-02-01', '2022-02-02', '2023-01-01', '2023-01-02', '2023-02-01', '2023-02-02', '2022-01-01', '2022-01-02', '2022-02-01', '2022-02-02', '2023-01-01', '2023-01-02', '2023-02-01', '2023-02-02'],
        'location': ['서울', '서울', '부산', '부산', '대구', '대구', '서울', '서울', '서울', '서울', '서울', '서울', '서울', '서울', '부산', '부산', '부산', '부산', '부산', '부산', '부산', '부산'],
        'PM10': [50, 40, 45, 55, 60, 65, 50, 40, 45, 55, 60, 65, 70, 80, 55, 45, 50, 60, 70, 75, 80, 90],
        'PM2.5': [25, 20, 22, 28, 30, 35, 25, 20, 22, 28, 30, 35, 40, 45, 30, 25, 28, 35, 40, 42, 45, 50]}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

df_monthly = df.groupby('location').resample('D', on='date').mean(numeric_only=True)
print(df_monthly)

df_monthly2 = df.groupby('location').resample('M', on='date').mean(numeric_only=True)
print(df_monthly2)

df_monthly3 = df.groupby('location').resample('Q', on='date').mean(numeric_only=True)
print(df_monthly3)





import matplotlib.pyplot as plt
import numpy as np

# x, y 데이터 생성
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# 선 그래프 그리기
plt.plot(x, y, color='red', linestyle='--', linewidth=2, marker='o', markersize=5)

# 그래프 타이틀과 축 라벨 설정
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('y')

# 그래프 출력
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# x, y 데이터 생성
x = np.random.rand(100)
y = np.random.rand(100)

# 산점도 그리기
#plt.scatter(x, y)
plt.scatter(x, y, color='red', marker='o', s=50, alpha=0.5)


# 그래프 타이틀과 축 라벨 설정
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')

# 그래프 출력
plt.show()



import matplotlib.pyplot as plt
import numpy as np

# 2x2 서브플롯 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 2x2 서브플롯 생성
fig, axs = plt.subplots(2, 2, figsize=(8, 8))

# 첫 번째 서브플롯
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sine')

# 두 번째 서브플롯
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cosine')

# 세 번째 서브플롯
axs[1, 0].plot(x, y1 + y2)
axs[1, 0].set_title('Sine + Cosine')

# 네 번째 서브플롯
axs[1, 1].plot(x, y1 - y2)
axs[1, 1].set_title('Sine - Cosine')

plt.show()

"""


import pandas as pd

# 데이터 파일 경로
data_path = '일별평균대기오염도_2022.csv'

# CSV 파일 읽기
df = pd.read_csv(data_path, encoding="cp949")

# 필요한 필드 추출
df = df[['측정일시', '측정소명', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']]

# 결측치 처리
df = df.dropna()

# 측정일시 컬럼의 데이터 타입을 datetime으로 변경
df['측정일시'] = pd.to_datetime(df['측정일시'], format='%Y%m%d')

print(df.head(20))

# import matplotlib.pyplot as plt

# # 연도별 미세먼지와 초미세먼지 농도 평균 계산
# df_monthly = df.resample('M', on='측정일시').mean(numeric_only=True)

# # 그래프 그리기
# plt.plot(df_monthly.index.month, df_monthly['미세먼지농도(㎍/㎥)'], label='PM10')
# plt.plot(df_monthly.index.month, df_monthly['초미세먼지농도(㎍/㎥)'], label='PM2.5')
# plt.legend()
# plt.xlabel('Month')
# plt.ylabel('Concentration')
# plt.title('2022 Air Pollution Trend')
# plt.show()

# import matplotlib.pyplot as plt

# # 일별 합계 계산
# df_daily = df.resample('D', on='측정일시').sum(numeric_only=True)

# # 일평균 대기오염도 계산
# df_daily['미세먼지농도(㎍/㎥)'] /= 24
# df_daily['초미세먼지농도(㎍/㎥)'] /= 24

# # 그래프 그리기
# plt.plot(df_daily.index, df_daily['미세먼지농도(㎍/㎥)'], label='PM10')
# plt.plot(df_daily.index, df_daily['초미세먼지농도(㎍/㎥)'], label='PM2.5')
# plt.legend()
# plt.xlabel('Date')
# plt.ylabel('Concentration')
# plt.title('2022 Air Pollution Trend')
# plt.show()


import matplotlib.pyplot as plt

# 지역별 미세먼지와 초미세먼지 농도 평균 계산
df_area = df.groupby('측정소명').mean(numeric_only=True).head(10)

# 그래프 그리기
plt.bar(df_area.index, df_area['미세먼지농도(㎍/㎥)'], label='PM10')
plt.bar(df_area.index, df_area['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Area')
plt.ylabel('Concentration')
plt.title('Air Pollution by Area')
plt.show()


import pandas as pd

# 데이터 파일 경로
data_path = '일별평균대기오염도_2022.csv'

# CSV 파일 읽기
df = pd.read_csv(data_path, encoding='cp949')

# 필요한 필드 추출
df = df[['측정일시', '측정소명', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']]

# 결측치 처리
df = df.dropna()

# 측정일시 컬럼의 데이터 타입을 datetime으로 변경
df['측정일시'] = pd.to_datetime(df['측정일시'], format='%Y%m%d')

# 이상치를 모아서 result.csv 파일로 저장
q1 = df['미세먼지농도(㎍/㎥)'].quantile(0.25)
q3 = df['미세먼지농도(㎍/㎥)'].quantile(0.75)
iqr = q3 - q1
outlier_df = df[(df['미세먼지농도(㎍/㎥)'] < q1 - 1.5 * iqr) | (df['미세먼지농도(㎍/㎥)'] > q3 + 1.5 * iqr)]
#outlier_df.to_csv('result.csv', index=False, encoding='utf-8-sig')







