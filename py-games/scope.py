def enemy_generation_1():
    print(enemy_num)


def enemy_generation_2(enemy_num):
    x = 3
    while x > 0:
        enemy_num += 1   # python interprets this as a local variable, and realises it is not been assigned a number
        print(enemy_num)
        x -= 1


enemy_num = 1
enemy_generation_2(enemy_num)

