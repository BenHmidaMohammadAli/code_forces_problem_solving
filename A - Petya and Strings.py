# https://codeforces.com/contest/112/problem/A

s1 = input().lower()
s2 = input().lower()

print(0 if s1 == s2 else 1 if s2 < s1 else -1)