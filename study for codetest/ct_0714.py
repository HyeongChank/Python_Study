
num = int(input())

# fibo = [0] * num
# print(fibo)

# fibo[0] = 0
# fibo[1] = 1
# print(fibo)
# for i in range(2,num):
#     fibo[i] = fibo[i-2] + fibo[i-1]
#     print(fibo)
# print(fibo[-1])


def fibona(num):
    if num <=1:
        return num
    else:
        return fibona(num-1) + fibona(num-2)

print(fibona(num))