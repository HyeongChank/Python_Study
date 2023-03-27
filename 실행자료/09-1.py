import pandas as pd
#한글 깨지는 거 방지하기 위해 encoding = "cp949"
df = pd.read_csv('일별평균대기오염도_2022.csv', encoding="cp949")
"""
print(df.info())

print(df.head())            # 상위 5개 데이터 출력
print(df.tail())            # 하위 5개 데이터 출력
print('\n', "기술 통계 출력===============================================")
print(df.describe())        # 수치형 열의 기술 통계 정보 출력

print("dfcol==================================================", '\n', df.columns)           # 열 이름 출력
print(df.index)             # 행 인덱스 출력
print('\n')
print("datatype================================================== " , df.dtypes, '\n')            # 열의 데이터 타입 출력
print("datashape================================================== ", df.shape, '\n')             # 데이터프레임의 크기 출력
print(df.isnull().sum())    # 결측치 개수 출력
"""

#복수조건
sub_df_1 = df.loc[(df['미세먼지농도(㎍/㎥)'] >200) & (df['초미세먼지농도(㎍/㎥)'] > 40) ,
                   ['측정소명','미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']]
print(sub_df_1)

# ##그래프 그리기
import matplotlib.pyplot as plt

import matplotlib
print(matplotlib.matplotlib_fname())
import os

# #한글 폰트 설정하기 : file - preference - setting - font - malgun gothic 추가


plt.plot(sub_df_1['측정소명'], sub_df_1['미세먼지농도(㎍/㎥)'], 'o-', label='미세먼지농도')

 # 그래프 제목 설정
plt.title('미세먼지농도(㎍/㎥)')

 # x축 레이블 설정
plt.xlabel('location')

 # y축 레이블 설정
plt.ylabel('미세먼지농도(㎍/㎥)')
 # plt.ylim([12, 15])

 # 그래프 출력
plt.show()











