n=int(input)

minPassenger=0
passenger=0

for index in range(n):
    exit,enter=map(int,input().split())
    passenger=(passenger+enter)-exit
    minPassenger=max(minPassenger,passenger)
print(minPassenger)