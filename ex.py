from ex1 import Calcul
class MoreCalcul(Calcul):
    def pow(self):
        return self.first ** self.second
a=MoreCalcul(5,3)
print(a.pow())
