for i in range(7):
    print(i)
print("***********")
sum=0
for j in range(0,100,2):
    sum+=j
print("sum : {}".format(sum))
print("***********")
sum=0
for k in range(11):
    if k<10:
        print("{} +".format(k),end=" ")
    elif k == 10:
        print("{}".format(k),end=" ")
    sum+=k
print("= {}".format(sum))
