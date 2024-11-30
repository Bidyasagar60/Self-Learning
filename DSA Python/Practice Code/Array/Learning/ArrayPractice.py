Expenses=[2200,2350,2600,2130,2190]


### Q1: 1. In Feb, how many dollars you spent extra compare to January? ###

print(f''' Extra dollars spent in Feb as compare to Jan: {Expenses[1]-Expenses[0]} ''')

### Q2. Find out your total expense in first quarter (first three months) of the year. ###

print(f''' Total Expeses of First Quarter: {Expenses[0]+Expenses[1]+Expenses[2]} ''')

### Q3. Find out if you spent exactly 2000 dollars in any month ###

Flag=False
for n,Exp in enumerate(Expenses):
    if Exp==2000:
        Flag=True
        exit
print(f"Did if speed 2000 Dollar in any month:{Flag}")

### Q4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list ###

Expenses.append(1980) 
print(Expenses)

### Q5. You returned an item that you bought in a month of April and ###
### got a refund of 200$. Make a correction to your monthly expense list

Expenses[3]=Expenses[3]-200
print(Expenses)
