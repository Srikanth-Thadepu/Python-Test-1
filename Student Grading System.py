student_name=input("Enter Student's name: ")
hindi=int(input('Marks in Hindi: '))
eng=int(input('Marks in English: '))
math=int(input('Marks in Maths: '))
science=int(input('Marks in Science: '))
social=int(input('Marks in Social: '))
max_marks=500
obtained_marks=hindi+eng+math+science+social
percentage=(obtained_marks/max_marks)*100
print("Total marks obtained: ",obtained_marks)
print('Total Percentage: ',percentage)
if percentage>80:
    print('A grade')
elif percentage>60:
    print('B garde')
elif percentage>40:
    print('C grade')
else:
    print('Fail')