def uppercase(s):
    uc=0
    for i in s:
        if i==i.upper():
            uc+=1
    return uc
def lowercase(s):
    lc=0
    for i in s:
        if i==i.lower():
            lc+=1
    return lc
def digits(s):
    digi='1234567890'
    d=0
    for i in s:
        if i in digi:
            d+=1
    return d
def special_character(s):
    special="~`!@#$%^&*()_+-=',./<>?;:"
    sc=0
    for i in s:
        if i in special:
            sc+=1
    return sc

def main():
    s=input("Enter the password: ")
    if len(s)>=8:
        if uppercase(s)<1 or lowercase(s)<1 or digits(s)<1 or special_character(s)<1:
            print("Weak Password")
        else:
            print('Strong Password')
    else:
        print('Must contain atleast 8 characters')
main()