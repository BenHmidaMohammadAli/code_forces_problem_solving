# https://codeforces.com/contest/231/problem/A

n = int(input())

problem = 0

for i in range (n):
    a =  map(int, input().split())
    if sum(a)>1 :
        problem += 1

print(problem)
