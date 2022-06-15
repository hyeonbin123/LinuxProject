def cal_def(i,k,p):
    if p == '+':
        print(i+k)
    elif p == '-':
        if i>k:
            print(i-k)
        elif k>i:
            print(k-i)
    elif p == '*':
        print(i*k)
    elif p == '/':
        if i>k:
            print(i/k)
        elif k>i:
            print(k/i)
x=int(input("1st number. "))
y=int(input("2nd number. "))
z=input("operator.(+, -, *, /) ")
cal_def(x,y,z)
