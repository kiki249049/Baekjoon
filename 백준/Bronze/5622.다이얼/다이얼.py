a=input()
time=0
for i in a :
    if ord(i) == 65 or ord(i) == 66 or ord(i) ==67 :
        time += 3
    elif ord(i) == 68 or ord(i) ==69 or ord(i) ==70 :
        time += 4
    elif ord(i) == 71 or ord(i) ==72 or ord(i) == 73 :
        time += 5     
    elif ord(i) == 74 or ord(i) ==75 or ord(i) ==76  :
        time += 6
    elif ord(i) == 77 or ord(i) ==78 or ord(i) ==79 :
        time += 7
    elif ord(i) == 80 or ord(i) ==81 or ord(i) ==82 or ord(i) ==83 :
        time += 8
    elif ord(i) == 84 or ord(i) ==85 or ord(i) ==86 :
        time += 9
    elif ord(i) == 87 or ord(i) ==88 or ord(i) ==89 or ord(i) ==90 :
        time += 10
    else :
        time += 11
print(time)               