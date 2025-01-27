n=int(input("Enter the value of n: "))
for i in range(1,n+1):
    print(i*'*')
print('Do you want reverse pattern too??')
r=int(input())
if r==1:
    for i in range(n,0):
        print(i*'*')