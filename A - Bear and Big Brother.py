# https://codeforces.com/contest/791/problem/A

a, b = map(int, input().split())
i = 0

while a<=b  :
    i+= 1
    a = a * 3
    b = b * 2

print(i)