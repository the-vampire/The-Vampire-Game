'''
定义一个吸血鬼类，继承人类，吸血鬼每天必须喝血，否则生命值减少30，
吸血鬼的移动速度是人类的4倍，
'''
import time
class Vampire(Person):
    time1 = time.time()

    def __init__(self):
        self.speed = 120
        while True:
            if time.time() - time1 == 60*60*4:
                self.hp -= 30

    def eat(self):
        if self.hp < 100:
            self.hp += 10
        if self.hp >= 100:
            self.hp = 100


    def help1(self, person):
        print("吸血鬼救助")
        self.hp = 100
        person == Vampire()
