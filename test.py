class game:
    def __init__(self,name,hp,ad):
        self.name,self.hp,self.ad=name,hp,ad
    def at(self,target):
        print(self.name+"가",target.name+"를 공격했습니다")
        target.hp-=self.ad
        print("{}의 체력이 {}에서 {}이 되었습니다.".format(target.name,target.hp+self.ad,target.hp))
man1=game("검사",100,10)
man2=game("검사",100,10)
man1.at(man2)
