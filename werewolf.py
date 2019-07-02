'''
定义一个狼人类，继承人类，移动速度是人类的4倍，每个月满会变身狼人，
撕咬方式会对人类及吸血鬼造成伤害，没有狼人的救助，被咬的人在第二天
会死亡

'''
import time
class Werewolf(Person):
    def __init__(self):
        self.speed = 120

    def help2(self):
        print("狼人救助")
        self.hp = 100


    def bite(self, people):
        time2 = time.time()
        while True:
            if time.time() - time2 == 60*60*2:
                people.hp = 0

