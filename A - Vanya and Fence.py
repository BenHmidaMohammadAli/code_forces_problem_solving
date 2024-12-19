# https://codeforces.com/contest/677/problem/A

	# CF677-D2-A

    
n,h = map(int, input().split())
a =  map(int, input().split())

total = 0
for i in a :
    if i> h:
        total+= 2
    else :
        total+= 1

print(total)

