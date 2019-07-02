'''
定义一个女巫变量，可以封禁狼人和吸血鬼的特异能力，
'''


class Necromancer(Person):
    def magic(self):
        self.speed = 0
