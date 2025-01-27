number_list=list(map(int,input('Enter the list of numbers: ').split()))
even=[]
odd=[]
for i in number_list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('Even list: ',even)
print('Odd list: ',odd)