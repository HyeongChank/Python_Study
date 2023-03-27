"""try:
    user_input = input("Enter a number: ")
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")


try:
    with open("non_existing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist. Please check the file path.")

try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")


try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")


try:
    # 예외가 발생할 수 있는 코드를 실행합니다.
except ExceptionType as error:
    # 예외가 발생했을 때 실행할 코드를 작성합니다.
    print(f"An error occurred: {error}")


try:
    result = 5 / 0
except ZeroDivisionError as error:
    print(f"An error occurred: {error}")
   

--------------------------------------------------------------
Exception
파이썬에서 모든 예외 클래스의 기본 클래스입니다. 이 클래스를 사용하면 어떤 종류의 예외든 처리할 수 있습니다.

try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except Exception as e:
    print(f"An error occurred: {e}")
--------------------------------------------------------------


try:
    user_input = input("Enter a number: ")
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print(f"You entered the number {number}.")
    
    
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name.")
except PermissionError:
    print("Permission denied. You don't have the required permission to read this file.")
else:
    print("File content:")
    print(content)
    file.close()
 

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name.")
except PermissionError:
    print("Permission denied. You don't have the required permission to read this file.")
else:
    print("File content:")
    print(content)
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File has been closed.")



data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6} 
while True:
    try:
        st = input("enter")
        value = data[st]
        print(value)
    except KeyError:
        print("no")
        break


data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6} 
while True:
    st = input("enter")
    value = data.get(st, None)
    if value is not None:
        print(value)
    else:
        print("none")
        break



file = open("example.txt", "r")

# 파일 내용 전체를 읽습니다.
content = file.read()
print(content)
print("-----------------------------------")

"""



