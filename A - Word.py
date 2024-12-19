# https://codeforces.com/contest/59/problem/A

s = input()

print(s.upper()) if sum(1 for i in s if i.isupper()) > len(s)/2 else print(s.lower())