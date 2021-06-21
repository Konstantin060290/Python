# Task1_1_2
# print('Введите год:')
# year = input()
# if int(year) % 4 == 0:
#     print('Введенный год високосный')
# elif int(year) % 100 == 0 and int(year) % 400 == 0:
#     print('Введенный год високосный')
# else:
#     print('Введенный год не високосный')

# Task1_1_3
# print('Введите Имя:')
# name = input()
# print('Введите пол (Мужской/Женский:')
# sex = input()
# print('Введите возраст:')
# age = input()
#
#
# def age_check(check_age):
#     s = str(check_age)
#     # Последняя цифра
#     last_digit = int(s[-1])
#
#     if int(check_age) == 1 or (int(check_age)-1) % 10 == 0:
#         age_text = str('год.')
#         return age_text
#     elif last_digit>1 and last_digit<5:
#         age_text = str('года.')
#         return age_text
#     elif last_digit==0 or (last_digit>4 and last_digit<=9):
#         age_text = str('лет.')
#         return age_text
#
#
# def hello(def_name, def_sex, def_age):
#     if def_sex == 'Мужской':
#         return print('Его зовут ' + def_name + '. Ему ' + def_age + ' ' + age_check(def_age))
#     elif def_sex == 'Женский':
#         return print('Ее зовут ' + def_name + '. Ей ' + def_age + ' ' + age_check(def_age))
#
#
# hello(name, sex, age)
# while True:
#     flag = input('Ещё раз? [да/нет]: ')
#
#     if flag == 'да':
#         print('Введите Имя:')
#         name = input()
#         print('Введите пол (Мужской/Женский:')
#         sex = input()
#         print('Введите возраст:')
#         age = input()
#         hello(name, sex, age)
#     else:
#         break

# Task1_1_4

# def factorial():
#     print('Введите число, факториал которого необходимо вычислить:')
#     n = input()
#     result = 1
#     for i in range(1, int(n) + 1):
#         result = result * i
#     print(result)
#
# factorial()
#
#
# while True:
#     flag = input('Ещё раз? [да/нет]: ')
#     if flag == 'да':
#         factorial()
#     else:
#         break

# Task1_1_5


# def numerics_with_uq_numbers():
#     n = 1000
#     for i in range(n, 9999):
#         n = n + 1
#         l = str(n)
#         if int(l[0]) != int(l[1]) and int(l[0]) != int(l[2]) and int(l[0]) != int(l[3]) and int(l[1]) != int(l[2]) and int(l[1]) != int(l[3]) and int(l[2]) != int(l[3]):
#             print(l)
#
#
# numerics_with_uq_numbers()

print('Введите конец диапазона для вывода простых чисел:')
n = int(input())
for i in range(1, int(n)+1):
     for k in range (2, int(n)):
        if int(i)%int(k)!=0 and int(i)%2 != 0 :
            print(i)
            break