import sys

N=int(input())

arr=list(map(int,sys.stdin.readline().split()))
max_num=0
asc_answer=[]
asc_len_box=[]
dec_answer=[]
dec_len_box=[]
for i in arr :
    if i >= max_num :
        asc_answer.append(i)
        max_num = i
    else :
        asc_len_box.append(len(asc_answer))
        asc_answer = []
        asc_answer.append(i)
        max_num = i
asc_len_box.append(len(asc_answer))
max_num=0
arr=arr[::-1]
for i in arr :
    if i >= max_num :
        dec_answer.append(i)
        max_num = i
    else :
        dec_len_box.append(len(dec_answer))
        dec_answer=[]
        dec_answer.append(i)
        max_num = i
dec_len_box.append(len(dec_answer))
if max(asc_len_box) > max(dec_len_box) :
    print(max(asc_len_box))
else :
    print(max(dec_len_box))
