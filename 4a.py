def swap_case(s):
    p=""
    for i in s:
        if i.islower():
            p=p+i.upper()
        elif i.isupper():
            p=p+i.lower()
        else:
            p=p+i
    return p
st=input()
print(swap_case(st))

