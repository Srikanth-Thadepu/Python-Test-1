salary=int(input("Enter your Salary Per Annum: "))
age=int(input('Enter your Age: '))
credit_score=int(input('Enter your Credit Score: '))
if salary>=400000 and age>=25 and credit_score>=750:
    print("Congratulations!! Your Loan is Approved")
else:
    if salary<400000:
        print("Sorry.... Your Loan is Rejected as your salary does not reach our requirement.")
    elif age<25:
        print("Sorry.... Your Loan is Rejected as your age  does not reach our requirement.")
    elif credit_score<750:
        print("Sorry.... Your Loan is Rejected as your credit score  does not reach our requirement.")
