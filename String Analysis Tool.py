s=input('Enter the string: ')
v=0
c=0
d=0
sc=0
Vowels='aeiou'
Consonants='bcdfghjklmnpqrstvwxyz'
Digits='1234567890'
for i in s:
    if i in Vowels:
        v+=1
    if i in Consonants:
        c+=1
    if i in Digits:
        d+=1
    if i in '~!@#$%^&*()_+`-/?.,':
        sc+=1
print('No. of Vowels: ',v)
print('No. of Consonants: ',c)
print('No. of Digits: ',d)
print('No. of Special Characters: ',sc)
rev=''
for j in s:
    rev=j+rev
print("Reverse of the String is: ",rev)
