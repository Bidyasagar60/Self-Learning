
Word_Count={}
with open('poem.txt',mode='r') as file:
    for line in file:
        tokens=line.split(' ')
        for token in tokens:
            token=token.replace('\n','')
            if token in Word_Count:
                Word_Count[token]+=1
            else:
                Word_Count[token]=1

print(Word_Count)

