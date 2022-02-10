A,B=map(int,input().split())
T=int(input())
x=[0,B]
y=[0,A]
for i in range(T) :
    direction, position = map(int,input().split())
    area = []
    if direction == 0 :
        x.append(position)
    else :
        y.append(position)
x.sort()
y.sort()
for k in range(len(x)-1) :
    for j in range(len(y)-1) :
        area.append((x[k+1]-x[k])*(y[j+1]-y[j]))
print(max(area))