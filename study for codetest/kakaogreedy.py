def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery =0
    pickup = 0
    deliveries.reverse()
    pickups.reverse()
    for i in range(n):
        delivery += deliveries[i]
        pickup +=pickups[i]
        while delivery > 0 or pickup > 0:
            print('i ', i, 'delivery ', delivery, 'pickup ', pickup)
            delivery -= cap
            pickup -= cap
            answer += (n-i) * 2
            print(answer)
            
    
    return answer


# def solution(cap, n, deliveries, pickups):
#     deliveries.reverse()
#     pickups.reverse()
#     sum_d=0
#     sum_p =0
#     flag_d =0
    
#     for i in range(n):
#         sum_d += deliveries[i]
#         sum_p += pickups[i]
        

deliveries = [1, 0, 2, 0, 1, 0, 2]
pickups = [0, 2, 0, 1, 0, 2, 0]
answer = solution(2,7,deliveries, pickups)

print(answer)