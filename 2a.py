# Converting 12 hour format to 24 hour format
print("Enter the time value in 12-hour format hh:mm:ss(AM/PM) : ")
s=input()
l=len(s)
c=0
p=int(s[0]+s[1])
if p==12 and s[l-2]=='A':
    i=0
    t=0
    c=1
elif p<12 and s[l-2]=='P':
    p=12+p
    i=p%10
    t=p//10
    c=1
act=""    
if c==1:
    act=act+str(t)+str(i)
    for i in range(2,l-2):
        act=act+s[i]
else:
    for i in range(0,l-2):
        act=act+s[i]
print(act)
