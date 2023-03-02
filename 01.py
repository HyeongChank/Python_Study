"""import keyword
#예약어 확인하는 방법(변수명 사용 x)
print(keyword.kwlist)

a = 7/2
print(a)
b = round(a)
print(b)
c = 4.24e-3
print(c)

d = "3.14"
print(type(d))
d = float(d)
print(type(d))
d = int(d)
print(d)

z2 = complex(4,-2)
print(z2)
z3 = complex(4,-2)
print("곱하기 =", z2*z3)

string = "Hello, World!"
print(string[0]) # "H" 출력
print(string[7]) # "W" 출력

greeting = "Hello"
name = "John"
message = greeting + ", " + name + "!"
print(message) # "Hello, John!" 출력

string = "Hello, World!"
position = string.find("World")
print(position) # 7 출력

word = "spam"
repeated = word * 3
print(repeated) # "spamspamspam" 출력

num = 10
text = "apple"
print(str(num) + text)

#리스트
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])
fruits[1] = "orange"
print(fruits)

#딕셔너리
fruits = {"apple": 3, "banana": 2, "cherry": 5}
print(fruits)
print(fruits["banana"])
fruits["orange"] = 4
print(fruits)

a1 = (4-2j)
a2 = a1**2
print(a2)

a = [1, 2, 3, 4, 5]
b = "Hello, World!"
print(3 in a)  # True 출력
print(6 in a)  # False 출력
print("o" in b)  # True 출력
print("k" not in b)  # True 출력


# 문자열 출력 예제
print("Hello, world!")  # "Hello, world!" 출력
print("My name is John.")  # "My name is John." 출력
print('The "quick brown" fox jumps over the lazy dog.')  # 'The "quick brown" fox jumps over the lazy dog.' 출력
print("I'm a boy.")  # "I'm a boy." 출력
print("He said, \"Hello!\"")  # "He said, "Hello!"" 출력
print("10"+"20") #문자열 잇기  1020
print("abc " * 3) #문자열 3번 출력  abc abc abc

# 변수 출력 예제
x = 10
y = 5
z = x + y
print(x, y, z)  # 10 5 15 출력

print(10+20)  # 30

# % 연산자를 이용한 포매팅
name = "John"
age = 30
height = 175.5

print("My name is %s, I'm %d years old, and my height is %4.2f." % (name, age, height))


# 진수 변환
decimal_num = 10
binary_num = bin(decimal_num)
print("The decimal number %d is equal to the binary number %s." % (decimal_num, binary_num))

# format() 메소드를 이용한 포매팅
name = "John"
name = "bob"
age = 30+3
height = 175.5+5

print("My name is {}, I'm {} years old, and my height is {:10.3f}.".format(name, age, height))
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."
print("My name is {1}, I'm {0} years old, and my height is {2:.1f}.".format(name, age, height))
print(f"My name is {age}, I'm {age} years old, and my height is {height:.1f}.")


name = "Tom"
age = 20
print(f"My name is {name} and I am {age} years old")

num = {"apple":3, "orange":2, "banana":1}
num2 = [100,20,3]
a = num["apple"]
o = num["orange"]
b = num["banana"]
print(f"I have {num['apple']} apples, {num2[0]} oranges, and {b} banana")

score = 1.23
print("The result is {}".format(num["apple"]))

score = 90
print("Your score is %d"%(score),"%")

num1 = int(input("first num:"))
num2 = int(input("second num:"))
print(f"{num1} + {num2} = {num1 + num2}")

# input()과 산술식만을 이용하여 가장 큰 숫자 출력하기
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
num3 = int(input("세 번째 숫자를 입력하세요: "))

max_num = num1

if max_num < num2:
    max_num = num2

if max_num < num3:
    max_num = num3

print(f"입력한 숫자 중 가장 큰 수는 {max_num}입니다.")"""


"""price = 100
count = int(input("개수"))
tax = 0.1
print(f"총 가격은 tax 포함 {price*count + price*count*tax:.4f} 입니다")


second = int(input("초를 입력하시오"))
minute = second//60
rsecond = second%60
print(f"{second}초는 {minute}분과 {rsecond}초 입니다")"""

"""total = int(input("분을 입력하시오"))
htransm = 60
dtransm = htransm*24
day = total//dtransm
rmin = total%dtransm
hour = rmin//htransm
rmhour = rmin%htransm

print(f"{day}일 {hour} 시간 {rmhour}분입니다 ")

"""
won = 500
rate = 0.05
totalr = 1+rate
year1 = won * (1+rate)
year2 = year1*(1+rate)
finalwon = won * (1+rate)**5
totalr2 = 0;

#print(year1, year2 , finalwon)

#print(f"5년 후 금액은 {finalwon:.3f} 입니다")

for i in range(1,6):
     totalr2 = totalr2*i
print(totalr2)
print(totalr**5)
"""num = int(input("숫자"))
cal = num*(num+1)/2
print(f"숫자의 합은 {cal} 입니다")

grape = 75
berry = 113.5
ngrape = int(input("포도알 개수"))
nberry = int(input("딸기알 개수"))
print(f"포도알 {ngrape} 개와 딸기알 {nberry} 개의 무게는 {grape*ngrape + berry*nberry:.0f} 입니다")
"""









    




