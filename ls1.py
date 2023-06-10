# # # посчитать кол-во отдельных символов
# # # aabb    a - 2    b - 2 
from time import time
# # # N ** 2
# # # def strcounter(data): 
# # #     start = time()
# # #     for sym in data:
# # #         count = 0
# # #         for sym_2 in data:
# # #             if sym == sym_2:
# # #                 count += 1
# # #         print(sym, count)
# # #     print( time() - start )




# # # strcounter("aaaabcd")





# # # N * M
# # def strcounter(data): 
# #     start = time()

# #     for sym in set(data): # len(set(data)) - N
# #         count = 0
# #         for sym_2 in data: # len(data) - M
# #             if sym == sym_2:
# #                 count += 1
# #         print(sym, count)
# #     print( time() - start )




# # strcounter("aaaabcd")


# # set - множество, тип данных, в котором только уникальные значения, неупорядоченные
# # f = set()
# # f = {1,1,2,3}
# # print(f)



# # f = set("aabhsdabdbaufb")

# # print(f)









# N
def strcounter(data): 
    start = time()
    sym_count = {} # dict
    for sym in data: # len(set(data)) - N
        # я беру символ или добавляю его если нету
        # беру кол-во символа и увеличиваю на 1 , а если его нету то ствалю 1
        sym_count[sym] = sym_count.get(sym, 0) + 1

    for s,c in sym_count.items(): # items - преобразую словарь в кортеж

        print(s,c)

    print( time() - start )




strcounter("aaaabcd")


# https://desktop.github.com/ - приложение гитхаба
# https://git-scm.com/ - для терминала
#   14:40 - 14:50

#git config --global user.name 'pavel' 
# git config --global user.email 'pavel@mail.ru' 

# git config --list    - проверяю настройки

# git init - создаем окальный репозиторий

# git add . - добавляю все файлы для отправки

# git remote add origin https://github.com/RyT32/testss.git
# git branch -M main
# git push -u origin main
# new
