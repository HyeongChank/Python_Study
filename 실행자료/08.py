"""
file = open("example.txt", "r")

# 파일 내용 전체를 읽습니다.
content = file.read()
print(content)
print("-----------------------------------")


# 파일에서 한 줄을 읽습니다.
file = open("example.txt", "r")
line = file.readline()
print("Line" , line)

# 파일 전체를 읽고 각 줄을 리스트로 반환합니다.
file = open("example.txt", "r")
lines = file.readlines()
print(lines)

file.close()  # 파일을 닫습니다.



with open("example.txt", "r") as file:
    # 파일 내용 전체를 읽습니다.
    content = file.read()
    print("read() 함수 예시:")
    print(content)

    # 파일에서 한 줄을 읽습니다.
    file.seek(0)  # 파일 포인터를 처음으로 돌립니다.
    line = file.readline()
    print("\nreadline() 함수 예시:")
    print(line)

    # 파일 전체를 읽고 각 줄을 리스트로 반환합니다.
    file.seek(0)  # 파일 포인터를 처음으로 돌립니다.
    lines = file.readlines()
    print("\nreadlines() 함수 예시:")
    print(lines)

# w = write, a = add, r = read
file = open("example2.txt", "a+")

# 파일에 문자열을 씁니다.
file.write("Hello, world!\n")
file.write("This is an example file.\n")

# 파일에 문자열의 리스트를 씁니다.
lines = ["We will use it to demonstrate file writing in Python.\n",
         "We can write multiple lines at once.\n"]
file.writelines(lines)

file.close()  # 파일을 닫습니다.


# 읽기 모드로 파일을 엽니다.
file = open("example.txt", "r")
content = file.read()
print("읽기 모드 예시:")
print(content)
file.close()

# 쓰기 모드로 파일을 엽니다.
file = open("example.txt", "w")
file.write("This is an example.\n")
file.write("We are writing to a file.\n")
print("쓰기 모드 예시:")
print("파일이 생성되었습니다.")
file.close()

# 추가 모드로 파일을 엽니다.
file = open("example.txt", "a")
file.write("We are appending to a file.\n")
print("추가 모드 예시:")
print("파일이 열렸고 내용이 추가되었습니다.")
file.close()


# 배타적 생성 모드로 파일을 엽니다.
file = open("example3.txt", "x")
file.write("This is a new file.\n")
print("배타적 생성 모드 예시:")
print("새로운 파일이 생성되었습니다.")
file.close()

# 이진 모드로 파일을 엽니다.
file = open("example.bin", "wb")
file.write(b"This is binary data.")
print("이진 모드 예시:")
print("바이너리 파일이 생성되었습니다.")
file.close()

# 읽기와 쓰기를 지원하는 모드로 파일을 엽니다.
file = open("example.txt", "r+")
content = file.read()
print("읽기와 쓰기를 지원하는 모드 예시:")
print("파일 내용:")
print(content)
file.write("\nWe are writing to the file again.")
file.close()

st = "aasdasdasdasdasd"


import re

# 문자열의 시작부터 정규표현식과 매칭되는 패턴 찾기
pattern = r"python"
string1 = "python is easy"
# 시작 부분에 없으면 못 찾음
string2 = "I love python"
string3 = "Python is fun"

match1 = re.match(pattern, string1)
match2 = re.match(pattern, string2)
match3 = re.match(pattern, string3)

if match1:
    print("매칭된 문자열:", match1.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match2:
    print("매칭된 문자열:", match2.group())
else:
    print("매칭되지 않음")

if match3:
    print("매칭된 문자열:", match3.group())
else:
    print("매칭되지 않음")

import re

# 문자열 전체에서 정규표현식과 매칭되는 패턴 찾기
# search는 문자열 전체
# [pP]는 대소문자 둘 다 해당한다는 의미
pattern = r"[pP]ython"

string1 = "python is easy"
string2 = "I love python"
string3 = "Python is fun"

match1 = re.search(pattern, string1)
match2 = re.search(pattern, string2)
match3 = re.search(pattern, string3)

if match1:
    print("매칭된 문자열:", match1.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match2:
    print("매칭된 문자열:", match2.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match3:
    print("매칭된 문자열:", match3.group())
else:
    print("매칭되지 않음")






import re

# 문자열에서 정규표현식과 매칭되는 모든 패턴 찾기
pattern = r"\d+"
file = open("example.txt", "r")
content = file.read()
matches21 = re.findall(pattern,content)
print(matches21)



string1 = "I have 2 apples and 3 oranges"
string2 = "The temperature is -1.45 degrees Celsius"
string3 = "The password is 12345678"

matches1 = re.findall(pattern, string1)
matches2 = re.findall(pattern, string2)
matches3 = re.findall(pattern, string3)

print(matches1)  # ['2', '3']
print(matches2)  # ['-1', '5']
print(matches3)  # ['12345678']


import re

# 문자열에서 정규표현식과 매칭되는 모든 패턴을 다른 문자열로 대체하기
pattern = r"\d+"
string1 = "I have 2 apples and 3 oranges"
string2 = "The temperature is -1.5 degrees Celsius"
string3 = "The password is 12345678"

result1 = re.sub(pattern, "10", string1)
result2 = re.sub(pattern, "0", string2)
result3 = re.sub(pattern, "***", string3)

print(result1)  # I have 10 apples and 10 oranges
print(result2)  # The temperature is -0.0 degrees Celsius
print(result3)  # The password is ***


import re

phone_number = "010-1234-5678"
#\d{3,4} 는 숫자 중 3글자 이상 4글자 이하인 것을 의미
pattern = r"(\d{2,3})-(\d{3,4})-(\d{4})"
result = re.match(pattern, phone_number)

area_code = result.group(1)
phone_number_without_area_code = result.group(2) + "-" + result.group(3)

print(area_code)  # 010
print(phone_number_without_area_code)  # 1234-5678


#그룹핑 치환
import re

date = "2022-03-18"
print(date)
pattern = r"(\d{4})-(\d{2})-(\d{2})"
result = re.sub(pattern, r"\2-\3-\1", date)

print(result)  # "03/18/2022"

string = "Kim, Yuna"
pattern = r"(\w+),\s*(\w+)"
result = re.sub(pattern, r"\2 ss \1", string)
print(result)  # "Yuna Kim"


string = Python is an interpreted language
Python It is dynamically typed
And it is easy to learn

# re.MultiLine은 줄단위로 찾음
import re

pattern = '^Python|typed$'
result = re.findall(pattern, string, re.MULTILINE)
print(result)  # ['Python', 'typed']



import re
# \. : '.'을 찾을 때 / {2, } : 2개 이상
def extract_email(string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, string)
    return emails

string = "khc's email is khc@gmail.com, John's email is john.doe123@example.com. Jane can be reached at jane@example.co.uk."

emails = extract_email(string)
print(emails)  # ['john.doe123@example.com', 'jane@example.co.uk']


string = "I love books. My favorite book is 'The Great Gatsby'."

import re

pattern = r'\bbook\b'
result = re.findall(pattern, string)
print(result)  # ['book']


import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email1 = 'example@example.com'
email2 = 'example@example.co.kr'
email3 = 'example.example.com'
email4 = 'example@example.'
email5 = 'example@example'

print(is_valid_email(email1))  # True
print(is_valid_email(email2))  # True
print(is_valid_email(email3))  # False
print(is_valid_email(email4))  # False
print(is_valid_email(email5))  # False


"""
import re

log_data = [
    '192.168.0.1 - - [21/Feb/2022:10:12:01 +0900] "GET /index.html HTTP/1.1" 200 2326',
    '192.168.0.2 - - [21/Feb/2022:10:12:02 +0900] "GET /images/banner.jpg HTTP/1.1" 200 6571',
    '192.168.0.3 - - [21/Feb/2022:10:12:03 +0900] "POST /login.php HTTP/1.1" 302 -',
    '192.168.0.4 - - [21/Feb/2022:10:12:04 +0900] "GET /favicon.ico HTTP/1.1" 404 209'
]

ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

for log in log_data:
    ip = re.findall(ip_pattern, log)
    print(ip)





