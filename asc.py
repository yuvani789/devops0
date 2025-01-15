n=int(input("enter num of elements"))
for i in range(n):
    a=int(input("enter element"))
    l.append(a)
print(l)
c=0
for i in l:
    if i>0:
        c+=1
if c==n:
    print("give -ve values")
for i in range(n-1):
    for j in range(1,n-1):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
        else:
            l[j],l[i]=l[i],l[j]
print(l)
for k in range(n-1,-1,-1):
    l1.append(l[k])
print(l1)


------------------------------
s=input()
s1=[char for char in s]
print(s1)
c=0
c1=0
c2=0
for i in range(len(s)):
    if 65<=ord(s[i])<=90:
        c+=1
    if 97<=ord(s[i])<=122:
        c1+=1
    if ord(s[i])==32:
        c2+=0
print(f'{c} caps')
print(f '{c1} smalls')
print(f '{c2} saces')
