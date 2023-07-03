
def solution(my_string):
    answer_list = my_string.split()
    sum =0
    sum = int(answer_list[0])

    for i in range(len(answer_list)):

        if answer_list[i]=='+':
            sum += int(answer_list[i+1])
        elif answer_list[i]=='-':
            sum -= int(answer_list[i+1])
    answer = sum 
    print(answer)   
    return answer

if __name__=="__main__":
    my_string = "3 + 4"
    solution(my_string)