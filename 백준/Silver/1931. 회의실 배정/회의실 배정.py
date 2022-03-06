import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    start, end = map(int, input().split())
    arr.append((start, end))
arr.sort(key=lambda x: x[0]) # x기준으로 정렬
arr.sort(key=lambda x: x[1]) # y기준으로 정렬

end = cnt = 0
for t in arr:
    if t[0] >= end:
        end = t[1]
        cnt += 1
print(cnt)