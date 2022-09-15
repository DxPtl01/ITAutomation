s=list(input().split(" "))
for i in range(0,len(s)):
    l=list(s[i])
    for j in range(0,len(l)):
        if j%2==0:
            print(l[j].upper(),end="")
        else:
            print(l[j].lower(),end="")
    print(" ",end="")
