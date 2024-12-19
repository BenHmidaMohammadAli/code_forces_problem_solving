# https://codeforces.com/contest/734/problem/A

n = int(input())
s = str(input())

s_a = 0
s_b = 0

for i in s: 
    if i =='A':
        s_a+= 1
    else:
        s_b+= 1

if s_a > s_b:
    print('Anton')
elif s_a < s_b:
    print('Danik')
else :
    print('Friendship')