#a year is a leap year if it is divisible by four, except for years that are divisible by 100 but not by 400
t=int(input('Enter the number of testcases: '))
for i in range(1,t+1):
    year=int(input('Enter the year: '))
    if (year%4 and year%10!=0) or year%400!=0:
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")