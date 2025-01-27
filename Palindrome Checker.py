n=int(input('Enter the number of inputs: '))
for i in range(n):
    s=input('Enter a string or a number: ')
    rev=''
    for i in s:
        rev=i+rev
    if s==rev:
        print('Palindrome')
    else:
        print('Not a Palindrome')