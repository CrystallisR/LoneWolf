import random
import math
import time

K = 999
CRT = [[[0,K],[0,K],[0,8],[0,6],[1,6],[2,5],[3,5]],
       [[0,K],[0,8],[0,7],[1,6],[2,5],[3,5],[4,4]],
       [[0,8],[0,7],[1,6],[2,5],[3,5],[4,4],[5,4]],
       [[0,8],[1,7],[2,6],[3,5],[4,4],[5,4],[6,3]],
       [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2]],
       [[2,6],[3,6],[4,5],[5,4],[6,4],[7,3],[8,2]],
       [[3,5],[4,5],[5,4],[6,3],[7,2],[8,2],[9,1]],
       [[4,4],[5,4],[6,3],[7,2],[8,2],[9,1],[10,0]],
       [[5,3],[6,3],[7,2],[8,0],[9,0],[10,0],[11,0]],
       [[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0]]]

def heartStr(num):
    hs = ""
    for i in range(0, num):
        hs += chr(10084) # choose your symbol #10084 heart
    return hs

class entity(object):
    def __init__(self, EP, CS) -> None:
        self.live = True
        self.EP = EP
        self.CS = CS
        
    def deadCheck(self):
        if self.live == False: 
            return True
        return False
        
    def deathAnnouncement(self):
        print("Is dead.\n")
        
    def changeStat(self, cEP= 0, cCS= 0):
        self.EP -= cEP
        self.CS -= cCS
        if self.EP <= 0 or cEP == K: self.live = False
        
    def showStat(self):
        if not self.deadCheck():
            print("Status:\nEndurance Point: %s\nCombat Skill: %d\n" %(heartStr(self.EP), self.CS))
        else: self.deathAnnouncement()
        
class protag(entity):
    def __init__(self, EP, CS) -> None:
        super().__init__(EP, CS)
        
    def deathAnnouncement(self):
        print("\033[1;32;40mLone Wolf\033[0m is dead.\n")
        
    def showStat(self):
        if not self.deadCheck():
            print("\033[1;32;40mLone Wolf\033[0m Status:\nEndurance Point: \033[1;31;40m%s\033[0m\nCombat Skill: %d" %(heartStr(self.EP), self.CS))
        else: self.deathAnnouncement()
        
class enemy(entity):
    def __init__(self, EP, CS, name) -> None:
        super().__init__(EP, CS)
        self.name = name
    
    def deathAnnouncement(self):
        print("\033[1;31;40m%s\033[0m is dead.\n" %self.name.title())
        
    def showStat(self):
        if not self.deadCheck():
            print("\033[1;31;40m%s\033[0m Status:\nEndurance Point: \033[1;31;40m%s\033[0m\nCombat Skill: %d" %(self.name.title(), heartStr(self.EP), self.CS))
        else: self.deathAnnouncement()

class combat(object):
    def __init__(self, pro, ene) -> None:
        self.pro = pro
        self.ene = ene
        
    def versus(self):
        random.seed(self.pro.CS * self.pro.EP)
        diff = self.pro.CS - self.ene.CS
        diff = diff if diff <= 0 else 0
        bias = random.randint(0, 9) - 1
        if bias == -1: bias += 10
        raw, column = bias, 0
        if diff <= -11: column = 0
        else: column = 6 - math.ceil(abs(diff)/2)
        eneMinus, proMinus = CRT[raw][column][0], CRT[raw][column][1]
        while not self.pro.deadCheck() and not self.ene.deadCheck():
            print("\n", end="")
            self.pro.changeStat(proMinus)
            self.ene.changeStat(eneMinus)
            self.pro.showStat()
            self.ene.showStat()
            time.sleep(1)
    
    def Versus(self):
        print("\n\033[1;33;40mCombat Start\033[0m:")
        self.versus()
        print("\033[1;33;40mCombat Over.\033[0m\n")
        
if __name__ == "__main__":
    lw = protag(22, 19)
    anEnemy = enemy(50, 12, "rogue")
    acombat = combat(lw, anEnemy)
    acombat.Versus()