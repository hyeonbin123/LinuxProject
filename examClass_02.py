class Embedded:
    def system(self,first,second):
        self.first=first
        self.second=second
a=Embedded()
b=Embedded()
a.system(3,5)
b.system(6,10)
print(a.first)
print(a.second)
print(b.first)
print(b.second)
