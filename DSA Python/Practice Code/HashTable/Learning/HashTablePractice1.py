import csv

TempList=[]
HashTab={}
with open('nyc_weather.csv',mode='r') as file:
    csvFile=csv.reader(file)
    for index,line in enumerate(csvFile):
        if(index !=0):
            TempList.append(int(line[1]))
            HashTab[line[0]]=int(line[1])
print(TempList)


Week1Temp=0

AVGWeek1Temp=sum(TempList[0:7])/ len(TempList[0:7])

print(f'Q1:Average Temp of Week1 of Jan :{AVGWeek1Temp}')
    
MaxTemp=max(TempList[0:10])

print(f'Q2: Maximum temperature in first 10 days of Jan:{MaxTemp}')


print(HashTab)
Jan9=HashTab['Jan 9']

Jan4=HashTab['Jan 4']

print(f'Weather on 9th Jan : {Jan9}')
print(f'Weather on 4th Jan : {Jan4}')
        