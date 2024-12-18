# https://codeforces.com/contest/263/problem/A


matrix = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            steps = abs(i + 1 - 3) + abs(j + 1 - 3)
            break

print(steps)
