print("Задача 1:")
n = int(input("Введите N"))
res = ''
for i in range(n):
    s = input()
    res = res + s + ''
print(res)


def zad2():
    slovo = input()
    res = ''
    while slovo != "stop":
            res = res + slovo + ' '
            slovo = input()
    print(res)


def zad3():
    slovo = input()
    if 'ф' in slovo:
        print("Ого! Это редкое слово!")
    else:
        print("Это обычное слово...")

def zad4():
    from random import randint
    m = 0
    r = 0
    while m < 3:
        a = randint(1,100)
        b = randint(1, 100)
        itog = int(input(str(a) + "+" + str(b) + "="))
        if a + b != itog:
                print("Ответ НЕ правильный!")
                m+=1
        else:
                print("Ответ правильный!")
                r+=1
    if m == 3:
        print("Игра окончена. Правильных ответов:", r)


"t7ut78i"


zad2()
zad3()
zad4()