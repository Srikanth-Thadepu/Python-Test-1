Total_bill=int(input("Enter the total bill amount: "))
friends=int(input('Enter the number of friends: '))
tip_percentage=int(input('Enter the tip percentage: '))
tip=tip_percentage*Total_bill/100
sum=Total_bill+tip
per_person=sum/friends
print('Each person has to pay: ',per_person)

