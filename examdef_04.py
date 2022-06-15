def cal_def(i,k,p):
    res=0
    if p == '+':
        res=i+k
    elif p == '-':
        if i>k:
            res=i-k
        elif k>i:
            res=k-i
    elif p == '*':
        res=i*k
    elif p == '/':
        if i>k:
            res=i/k
        elif k>i:
            res=k/i
    return res
x=int(input("1st number. "))
y=int(input("2nd number. "))
z=input("operator.(+, -, *, /) ")
res=cal_def(x,y,z)
print("res is {}.".format(res))
