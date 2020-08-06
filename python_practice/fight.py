"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""


def fight():  # 定义一个打斗的方法
    my_hp = 1000  # 我的初始血量为1000
    my_power = 100  # 我的初始攻击力为100
    enemy_hp = 1000  # 敌人的初始血量为1000
    enemy_power = 120  # 敌人的初始攻击力为120
    while True:  # 使用循环，实现多次打斗，直到一方血量小于等于零，break结束循环
        my_hp = my_hp - enemy_power  # 我的剩余血量 = 我的初始血量 - 敌人的攻击力
        enemy_hp = enemy_hp - my_power  # 敌人的剩余血量 = 敌人的初始血量 - 我的攻击力
        if my_hp <= 0:  # 判断我方血量是否小于等于零
            print("你输了")  # 打印出“你输了”
            break  # 跳出while循环
        elif enemy_hp <= 0:  # 判断敌方血量是否小于等于零
            print("你赢了")  # 打印出“你赢了”
            break  # 跳出while循环


fight()  # 调用fight方法
