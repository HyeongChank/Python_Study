# n = int(input())

# for i in range(n):
#     a,b = map(str, input().split())

#     def operate(a,b):
#         answer = []
#         for m in b:
#             am = m * int(a)
#             answer.append(am)
#         result = ''.join(answer)
#         print(result)
    
#     operate(a, b)
    
    
# n = int(input("숫자입력"))

# n_list = [i for i in range(1,n+1)]
# n_list.reverse()
# def operate(n_list):
#     while True:
#         if len(n_list) == 1:
#             break
#         n_list.pop()
#         add_num = n_list[len(n_list)-1]
#         n_list.pop()
#         n_list.insert(0, add_num)
    
#     result = n_list[0]
#     print(result)
# operate(n_list)



# from collections import deque

# queue = deque()
# num = int(input())
# for i in range(1, num+1):
#     queue.append(i)

# while True:
#     if len(queue) ==1 :
#         break
#     queue.popleft()
#     add_num = queue[0]
#     queue.popleft()
#     queue.append(add_num)
# print(queue[0])
    
# import math
# a,b,c = map(int, input().split())

# result = 0

# def operate(a,b,c):
#     global result
#     if a > 0:
#         a -= 1
     
#         size = 2 ** a
#         if c < size and b < size:
            
#             operate(a, b, c)
#         elif c >=size and b < size:
#             result += size * size
#             c -= size
#             operate(a,b,c)
#         elif c < size and b >= size:
#             result += 2*size * size
#             b -= size
#             operate(a,b,c)
#         elif c >= size and b >= size:
#             result += 3*size * size
#             c -= size
#             b -= size
#             operate(a,b,c)

            
# operate(a,b,c)
# print(result)
