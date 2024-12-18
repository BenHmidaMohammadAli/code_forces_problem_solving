# https://codeforces.com/contest/231/problem/A

n = int(input())

problem = 0

for i in range (n):
    a,b,c =  map(int, input().split())
    if a+b+c>1 :
        problem += 1

print(problem)
