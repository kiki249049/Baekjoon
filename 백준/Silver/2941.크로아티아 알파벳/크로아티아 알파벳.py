words=input()
counts=0
while len(words) > 0 :
    if 'c=' in words :
        counts += 1
        words=words.replace('c=',' ',1)
        continue
    elif 'c-' in words :
        counts += 1
        words=words.replace('c-',' ',1)
        continue
    elif 'dz=' in words :
        counts += 1
        words=words.replace('dz=',' ',1)
        continue
    elif 'd-' in words :
        counts += 1
        words=words.replace('d-',' ',1)
        continue
    elif 'lj' in words :
        counts += 1
        words=words.replace('lj',' ',1)
        continue
    elif 'nj' in words :
        counts += 1
        words=words.replace('nj',' ',1)
        continue
    elif 's=' in words :
        counts += 1
        words = words.replace('s=',' ',1)
        continue
    elif 'z=' in words :
        counts +=1
        words = words.replace('z=',' ',1)
        continue
    else :  
        if len(words) == 0 :
            break
        else :
            words=words.replace(' ','')
            counts += len(words)
            break
print(counts)