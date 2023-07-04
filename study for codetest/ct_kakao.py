from datetime import datetime


def solution(today, terms, privacies):
    index =0
    answer = []
    
    terms_dic = {}
    for i in terms:
        a, b = map(str, i.split())
        terms_dic[a] = b
    privacies_dic = {}
    for pv in privacies:
        index += 1
        a,b = map(str, pv.split())
        result_date = new_date(a, terms_dic[b])
        # print(result_date)
        # print(today)
        answers = compare_date(result_date, today, index, answer)

    return answers
def new_date(date, add_month):
    new_year = date[0:4]
    new_month = date[5:7]
    new_day = date[8:10]
    result_year = 0
    result_month =0

    if int(new_month) + int(add_month) > 12:
        result_year = int(new_year) + 1
        result_month = int(new_month) + int(add_month) -12
    else:
        result_year = int(new_year)
        result_month = int(new_month) + int(add_month)

    if result_month <10:
        result_date = str(result_year) + '.0' + str(result_month) + '.' +new_day
    else:
        result_date = str(result_year) + '.' + str(result_month) + '.' + new_day

    return result_date
        
def compare_date(date, today, index, answer):

    a_date = datetime.strptime(date, '%Y.%m.%d')
    b_date = datetime.strptime(today, '%Y.%m.%d')
    if a_date <= b_date :
        answer.append(index)    
    return answer
def solution(today, terms, privacies):
    answer = []
    year = today[0:4]
    month = today[5:7]
    date = today[8:10]
    return answer







if __name__=="__main__":
    
    pass