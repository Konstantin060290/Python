# Task_1_2_1
# print('Введите Фамилию')
# surname=input()
# print('Введите Имя')
# name=input()
# print('Введите Отчество')
# mid_name=input()
# print('Ваше имя: '+surname+' '+name[0]+'.'+mid_name[0]+'.')

# Task_1_2_2
print('Введите фразу содержащую цифры и буквы:')
string = input()
a = 0
numbers = ['0','1','2','3','4','5','6','7','8','9']
for i in range(0, len(string)):
    if  str(string[i]) in numbers:
        a += int(string[i])
print('Сумма цифр во фразе:')
print(a)