w=float(input('Enter the body weight in kilograms: '))
h=float(input('Enter the height in meters: '))
bmi=w/(h**2)
print('Your Body Mass Index is: ',bmi)
if 25<= bmi<=30:
    print('Overweight')
elif 18.5<=bmi<25:
    print("Healthy")
elif bmi<18.5:
    print('Underweight')