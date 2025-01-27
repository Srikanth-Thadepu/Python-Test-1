n=list(map(int,input('Enter the list of the numbers: ').split()))
n.sort()
n.pop()
print(max(n))