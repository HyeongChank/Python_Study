"""Kscore = int(input("국어 성적"))
Escore = int(input("영어 성적"))
Mscore = int(input("수학 성적"))
average = Kscore*0.4+Escore*0.4+Mscore*0.2
print("성적결과")

if average>=90:
    print("A")
elif average>=80:
    print("B")
elif average>=70:
    print("C")
elif average>60:
    print("D")
else:
    print("F")
  """  


"""length = int(input("길이를 입력하세요"))
inch = length/2.54
if length<0:
    print("잘못 입력하였습니다")
else :
    print(f"{inch:.0f} 인치입니다")
    
score = int(input("학점"))
if score<40:
    print("1학년입니다")

elif score<80:
    print("2학년입니다")
else :
    print("졸업반입니다")
    
    
Phour = int(input("현재시간"))
apm = input("am or pm")

ahead = int(input("how many hours ahead"))
newtime = Phour+(ahead%24)

if newtime>12:
    if apm == "am":
        apm == "pm"
    else :
        apm =="am"
    print("new hour", newtime%12, apm)

else:
    if apm == "am":
        apm == "am"
    else :
        apm =="pm"
    print("new hour", newtime%12, apm)  

        
enter = int(input("enter"))
while enter>0:
    print(f"{enter}는 0보다 크다")
    enter = enter+ 100
    if enter>500:
        break
      

num = int(input("10진수를 입력하세요"))
binary =""
while num>0:
    remain = num%2
    binary = str(remain)+binary
    num = num//2

print("입력한 수의 2진수 표현", binary)


fruits = ["apple","banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
numbers= [1,2,3,4,5]
sum =0
for num in numbers:
    sum +=num
print(sum)

for i in range(2,10,2):
    sum = sum+i
print(sum)
"""
"""기본적으로 print 안에 end="\n" 들어있음(줄 바꿈) 이것을 변경할 수 있다
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="")
    print()

num = int(input("정수입력"))
sum =0
for i in range(0,num+1, 3):
    sum += i
print(sum)
sum1 =0
for i in range(0,num+1, 5):
    sum1 += i
print(sum1)
print(f"{num}의 3의 배수와 5의 배수의 합 : {sum+sum1}")

'중복제거'
sum2 =0
for i in range(0, num+1):
    if i%3==0 or i%5 ==0:
        sum2 += i
print(f"{num}의 3의 배수와 5의 배수의 합 : {sum2}")
    


n2 = int(input("2번째 숫자 입력"))
n3 = int(input("3번째 숫자 입력"))
n4 = int(input("4번째 숫자 입력"))
n5 = int(input("5번째 숫자 입력"))
array = [n1, n2, n3, n4, n5]





max =0
min =110
for i in range(1,6,1):
    n = int(input(f"{i}번째 숫자 입력"))
    if n>max:
        max =n
    if n<min:
        min =n
print("최댓값 :", max)
print("최소값 :", min)
       
        
sum =0
for i in range (100):
    n = int(input(f"{i+1}번째 숫자 입력"))
    
    if sum<100:
        sum += n
        print(f"으로 합계{sum}이 됨")
        
    elif sum>=100:
        print("합계 100 넘음")
        break
     
sum =0
i=1
while sum<=100:
    
    n = int(input(f"{i}번째 숫자 입력"))
    sum+= n
    print(sum)
    i += 1
    
        
n1 =1
n2 =1
n3 = n1+n2
i=1;
num = int(input("몇 번째 항을 출력할까요?"))
while i<num-1:
    n3=n1+n2
    n1=n2
    n2=n3
    i+=1

print(f"피보나치 수열의 {num}번 째 항은 {n3}입니다")
       

vowels = ['a', 'e', 'i', 'o', 'u']
input_str = input("Enter a string: ")
output_str = ""
for char in input_str:
    if char in vowels:
        pass
    else:
        output_str += char

print("Modified string:", output_str)
  

import random

# 1부터 100 사이의 임의의 수를 선택합니다
secret_number = random.randint(1, 100)

while True:
    # 사용자가 숫자를 입력합니다
    guess = int(input("Guess the secret number (between 1 and 100): "))

    # 입력한 숫자와 비교합니다
    if guess < secret_number:
        print("Up")
    elif guess > secret_number:
        print("Down")
    else:
        print("Correct!")
        break  # 정답을 맞췄으므로 반복문을 종료합니다

대표적인 함수
random(): 0.0에서 1.0 사이의 실수 난수를 생성합니다.
randint(a, b): a 이상 b 이하의 정수 난수를 생성합니다.
randrange(start, stop[, step]): start 이상 stop 미만의 정수 중 step 간격으로 무작위로 선택된 값(정수)을 반환합니다.
choice(sequence): 주어진 시퀀스에서 임의의 항목을 반환합니다. 시퀀스는 문자열, 리스트, 튜플 등의 반복 가능한 객체입니다.
shuffle(x): 리스트 x의 항목을 무작위로 섞습니다.
sample(population, k): 시퀀스 자료형(population)에서 중복 없이 k개의 요소를 랜덤하게 뽑아 리스트로 반환하는 함수

import random
while True:
    d1 = random.randint(1,7)
    print(f"첫번째 다이스 숫자 {d1}입니다")
    d2 = random.randint(1,7)
    print(f"첫번째 다이스 숫자 {d2}입니다")
    if d1+d2 ==7:
        print("승리")
        break
    else:
        print("패배")
  
exit = 3
print(type(str(exit)))

while True:
    n1 = input("첫번째 수를 입력하세요")
    if str(n1) =="exit":
        print("종료")
        break
    n2 = int(input("두번째 수를 입력하세요"))
    x = input("연산자를 입력하세요 (+,-,*,/)")
    if x=="+":
        result = int(n1)+n2
        print(result)
    elif x=="-":
        result = int(n1)-n2
        print(result)
    elif x=="*":
        result = int(n1)*n2
        print(result)
    elif x=="/":
        result = int(n1)/n2
        print(result)
      
import random

m = 50

while m>0 and m<100:
    tf = int(input("앞뒤 선택"))
    coin = random.randint(1,2)
    if tf==coin:
        m+=19
        print(f"맞췄음 현재 금액 {m}")
    elif tf !=coin:
        m-=20
        print(f"틀렸음 현재 금액 {m}")
if m>=100:
    print("게임승리")
else:
    print("게임패배")
        
    
n1 = int(input("첫번째 숫자"))
n2 = int(input("두번째 숫자"))
if n1>n2:
    max = n1
    min = n2
else:
    max =n2
    min = n1
rem =1
while rem !=0:
    rem = max%min
    max = min
    min = rem
        
print(f"최대공약수는 {max}이다")

num = int(input("입력"))
for i in range(1,num+1):
    if num%i==0:
        print(i)
"""        
        
num = int(input("입력"))
for i in range(2, num+1):
    for j in range(2, num):
        if i%j ==0:
            print(i)

        
        

        
