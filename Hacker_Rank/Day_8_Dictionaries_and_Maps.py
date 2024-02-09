# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

n=int(input())
dict={}

for i in range(n):
    name,phone=input().split()
    dict[name]=phone
while True:
    try:
        name=input()
        if name in dict:
            print("{}={}".format(name,dict[name]))
        else:
            print("Not found")
    except EOFError:
        break
        
    