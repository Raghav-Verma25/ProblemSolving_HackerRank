n=int(input())
for i in range(0,n):
    s1=input()
    s=list(s1)
    p=s[::-1]
    assciilist1=[]
    for i in s:
        assciilist1.append(ord(i))
    assciilist2=assciilist1[::-1]
    sub=[]
    sub2=[]
    for i in range(0,len(assciilist1)-1):
        s=abs(assciilist1[i] - assciilist1[i+1])
        sub.append(s)
    for j in range(0,len(assciilist2)-1):
        s1=abs(assciilist2[j] - assciilist2[j+1])
        sub2.append(s1)
    if sub == sub2:
        print('Funny')
    else:
        print('Not Funny')
    
