class Calcul:
    def __init__(self,first,second):
        self.first,self.second=first,second
    def add(self):
        return self.first+self.second
    def mul(self):
        return self.first*self.second
    def sub(self):
        return self.first-self.second
    def div(self):
        return self.first/self.second
class MoreCalcul(Calcul):
    def pow(self):
        return self.first**self.second
a=MoreCalcul(int(input("1st : ")),int(input("2nd : ")))
print(a.pow())
b=MoreCalcul(int(input("1st : ")),int(input("2nd : ")))
print(b.pow())
