# https://codeforces.com/problemset/problem/977/A?mobile=false
num=int(input())
op=int(input())



def wrong_subtraction(num,operations):

    for operation in range(operations):
        if num%10==0:
            num=num//10
        else:
            num=num-1
    return num

print(wrong_subtraction(num,op))