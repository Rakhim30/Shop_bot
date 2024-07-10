from aiogram.fsm.state import State,StatesGroup

class My_State(StatesGroup):
    starts=State()
    s_shop = State()
    son = State()
    base = State()
    back = State()
    dele =State()
    a = State()
    adv = State()
    low = State()
    osh = State()

    ud = State()
    name = State()
    prise = State()
    imgg = State()
    dic = State()
    up = State()



# a = int(input())


# cnt = 0
# for i in range(0,101):
#     cnt += 1
#     if cnt == a:
#         if cnt<100 and cnt>10:
#             print('ishladi')
#     else:
#         print('bazada yoq')
