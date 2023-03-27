"""my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
if 'name' in my_dict:
    print(my_dict['name'])  # 'Alice'
if 'phone' in my_dict:
    print(my_dict['phone'])
  
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # 'Alice'
#print(my_dict['phone'])  # KeyError

"""
days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
#사용자가 월을 입력하면 해당 월에 일수를 출력하라
"""
m = input("월을 입력하시오")
print(m)

print(days[m.title()])

#알파벳 순서로 모든 월을 출력하라
dk = list(days.keys())
print(dk)
dks = sorted(dk)
print(dks)
 
#일수가 31인 월을 모두 출력하라
for x in days:
    if days[x] ==31:
        print(x)
#월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라
sorts = sorted(days.values())
print(sorts)

sortB = days.items()

#for x in days(days.keys(),days.values()):
 #   print(x)

print(sorted(sortB))    
sortB = [(day,month) for (month, day) in sortB]
print(sorted(sortB))
    
#사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
m3 = input("month3")
for x in days:
    print(x[:3])
    if x[:3] == m3.title():
       print(days[x])

d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},{'name':'Princess', 'phone':'555-3141', 'email':''},{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
   
#전화번호가 8로 끝나는 사용자 이름을 출력하라

for x in d:
    if x['phone'][7]=='8':
        print(x['name'])
        
#이메일이 없는 사용자 이름을 출력하라
for x in d:
    if x['email']=='':
        print(x['name'])        
#사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라
name = input("name : ")
flag =1
for x in d:
    if x['name'] == name.title():
        print(x['phone'], x['email'])
        flag =0;
if flag ==1:
    print("no name")
"""
"""
#set 중복제거
ms = set({1,2,3,3,3,})
print(ms)
ms = set([1,2,3,4,4,4])
print(ms)

ms = set()
ms.add(1)
ms.add(30)
print(ms)
ms.update([1,10,203])
print(ms)
ms.remove(10)
print(ms)
#존재하지 않아도 오류 x
ms.discard(300)
print(ms)
#존재하지 않으면 오류 ㅇ
ms.remove(300)
print(ms)

import random
pick = set()
lt = list()
#for x in range(7):
while len(pick)<6:
    
    pick.add(random.randint(1,46))
    lt.append(random.randint(1,46))
print(pick)
print(lt)
if len(lt)>6:
    print("중복 발생")
    
score = {
    "Alice": [85, 90, 95],
    "Bob": [75, 80, 85],
    "Charlie": [95, 95, 95]
}

print(score['Alice'])
print(score['Alice'][0])

#for x in score:
 #   for y in [x]:
  #      print(y)
#      sum += y
#print(sum)

for name, grade in score.items():
    print(name, sum(grade)/len(grade))

for n, s in score.items():
    print(n,s, sum(s), len(s))

d = [1, 2, 2, 3, 3, 3, 4, 4, 5]
setd = set(d)
print(setd)
print(sum(setd))

text = "Hello, world!"
lt = list(text)
print(lt)
 
dicT = {}
for char in text:
    print(dicT)
    if char not in dicT:
        dicT[char] = 1
    else:
        dicT[char] = dicT[char] +1
print(dicT)
   
def add_numbers(a,b):
    result = a+b
    return result

result = add_numbers(3,5)
print(result)

def du_numbers(a):
    result =1
    for i in range(1,a+1):
        result *=a
    return result
rs = du_numbers(10)
print(rs)

def square(a,b,c):
    result = a*b*c
    return result
sq = square(1,2,3)
print(sq)

def cir_area(r):
    result = r*r*3.14
    return result
def cir_cirm(r):
    result = 2*r*3.14
    return result
ca = cir_area(3.5)
cc = cir_cirm(3.5)
print(f'넓이 {ca:.1f} 둘레 {cc:.1f}')


        
def print_numbers(a, b, *args, c=10, d=20):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")
    print(f"args: {args}")

# 함수 호출
print_numbers(1, 2, 3, 4, 5, c=30, d=40)
# 출력 결과: a: 1, b: 2, c: 30, d: 40, args: (3, 4, 5)


x = 1  # 전역 변수
t = 'glo'
def my_function():
    y = 2  # 지역 변수
    print('y:', y)
    print('x:', x)
    t = 'bal'
    print(t)
    
    
my_function()
print('x:', x)
print(t)

def box(n,m):
    for j in range(m):
        for i in range(n):
            print("*", end="")
        print('\n')
box(3,4)

a = '123'
def sum(a):
    c = str(a)
    b = list(c)
    sum =0
    for i in b:
        sum +=int(i)
    print(sum)
result = sum(123)
print(result)

#def sum('a'):
    







    

x = 'global'

def outer():
    x = 'outer'
    
    def inner():
        x = 'inner'
        print('x in inner:', x)
    
    inner()
    print('x in outer:', x)

outer()
print('x in global:', x)
""" 
num = [4,5]
addl = list(filter(lambda a:a%2==0, num))
print(addl)
"""
dupl = lambda a,b:a*b
result = addl(3,4)
print(result)
result2 = dupl(3,4)
print(result2)
am = (1,2,3,4)
result = [i for i in am]
print(result)

addm = lambda a,b,c,d: a+b+c+d
result3 = addm(result)



print(result3)
#for i in 
#print(result3)





"""