def is_prime(z):
    for i in range(2,int(z**0.5)+1):
        if z%i==0:
            return False
    return True

def main():
    a=int(input('Enter the starting number of the range: '))
    z=int(input('Enter the ending number of the range: '))
    for i in range(a,z+1):
        if is_prime(i):
            print(i)
main()