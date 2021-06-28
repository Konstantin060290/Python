# Task_1_3_1
# alphabet = ['А','Б','В', 'Г', 'Д']
# a = 1
# for i in range (len(alphabet)):
#     for k in range (a):
#         print(alphabet[k], end=" ")
#     a += 1
#     print()

# Task_1_3_2
# m = input()
# n = input()
# x = 0
# for i in range(0, int(m)):
#     print("")
#     x += 1
#     y = 0
#     for k in range(0, int(n)):
#         y += 1
#         print(pow(x,y), end="/")

# Task_1_3_3
# Проверку на существование фигуры не выполнял
# import math
#
#
# class Point:
#     def __init__(self, coordinate_x, coordinate_y):
#         self.coordinate_x = coordinate_x
#         self.coordinate_y = coordinate_y
#
#
# Point_1 = Point(2, 1)
# Point_2 = Point(1, 3)
# Point_3 = Point(3, 6)
# Point_4 = Point(5, 3)
# Point_5 = Point(4, 1)
#
#
# def length_of_side(point1, point2):
#     length = math.sqrt(math.pow((point2.coordinate_x - point1.coordinate_x), 2)
#                        + math.pow((point2.coordinate_y - point1.coordinate_y), 2))
#     if (point2.coordinate_y == point1.coordinate_y):
#         length = point2.coordinate_x - point1.coordinate_x
#     if (point2.coordinate_x == point1.coordinate_x):
#         length = point2.coordinate_y - point1.coordinate_y
#     return length
#
#
# def triangle_area(length1, length2, length3):
#     p = (1 / 2) * (length1 + length2 + length3)
#     area = math.sqrt(p * (p - length1) * (p - length2) * (p - length3))
#     return area
#
#
# l1 = length_of_side(Point_1, Point_2)
# l2 = length_of_side(Point_2, Point_3)
# l3 = length_of_side(Point_3, Point_4)
# l4 = length_of_side(Point_4, Point_5)
# l5 = length_of_side(Point_5, Point_1)
# l6 = length_of_side(Point_3, Point_1)
# l7 = length_of_side(Point_3, Point_5)
# a1 = triangle_area(l1, l2, l6)
# a2 = triangle_area(l5, l6, l7)
# a3 = triangle_area(l3, l4, l7)
#
#
# fiveangle_area = a1 + a2 + a3
# print(fiveangle_area)


# Task_1_3_4
# rome_numbers = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII",
#                 9: "IX", 10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
#                 100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC",
#                 800: "DCCC", 900: "DM", 1000: "M", 2000: "MM", 3000: "MMM", 4000: "MMMM"}
# print("Ввведите число <=4000 для написания римскими цифрами:")
# num = input()
# # Проверки:
# # print(int(num[1]))
# # # print(list(rome_numbers.keys()))
# # print(str(rome_numbers.get(int(num[1])*100)))
# # print(list(rome_numbers.keys())[int(num[1])-1])
# if int(num) > 4000:
#     print("В задаче рассматриваются только числа <=4000")
# else:
#     if len(num) == 4:
#         if int(num[3]) == list(rome_numbers.keys())[int(num[3])-1]:
#             rome_num = str(rome_numbers.get(int(num[3])))
#         if int(num[3]) == 0:
#             rome_num = str("")
#         if int(num[2]) == list(rome_numbers.keys())[int(num[2])-1]:
#             rome_num2 = str(rome_numbers.get(int(num[2])*10))
#         if int(num[2]) == 0:
#             rome_num2 = str("")
#         if int(num[1]) == list(rome_numbers.keys())[int(num[1])-1]:
#             rome_num3 = str(rome_numbers.get(int(num[1])*100))
#         if int(num[1]) == 0:
#             rome_num3 = str("")
#         if int(num[0]) == list(rome_numbers.keys())[int(num[0])-1]:
#             rome_num4 = str(rome_numbers.get(int(num[0])*1000))
#         print(rome_num4+rome_num3+rome_num2+rome_num)
#
#     if len(num) == 3:
#         if int(num[2]) == list(rome_numbers.keys())[int(num[2])-1]:
#             rome_num = str(rome_numbers.get(int(num[2])))
#         if int(num[2]) == 0:
#             rome_num = str("")
#         if int(num[1]) == list(rome_numbers.keys())[int(num[1])-1]:
#             rome_num2 = str(rome_numbers.get(int(num[1])*10))
#         if int(num[1]) == 0:
#             rome_num2 = str("")
#         if int(num[0]) == list(rome_numbers.keys())[int(num[0])-1]:
#             rome_num3 = str(rome_numbers.get(int(num[0])*100))
#         print(rome_num3+rome_num2+rome_num)
#
#     if len(num) == 2:
#         if int(num[1]) == list(rome_numbers.keys())[int(num[1])-1]:
#             rome_num = str(rome_numbers.get(int(num[1])))
#         if int(num[1]) == 0:
#             rome_num = str("")
#         if int(num[0]) == list(rome_numbers.keys())[int(num[0])-1]:
#             rome_num2 = str(rome_numbers.get(int(num[0])*10))
#         print(rome_num2+rome_num)
#
#     if len(num) == 1:
#         if int(num[0]) == list(rome_numbers.keys())[int(num[0])-1]:
#             rome_num = str(rome_numbers.get(int(num[0])))
#         print(rome_num)

# Task_1_3_5
# from random import randint
# a1 = 0
# a2 = 0
# a3 = 0
# a4 = 0
# a5 = 0
# a6 = 0
# b1 = 0
# b2 = 0
# b3 = 0
# b4 = 0
# b5 = 0
# b6 = 0
#
# for i in range(1, 1001):
#
#     bone1 = randint(1, 6)
#     bone2 = randint(1, 6)
#     if bone1 == 1:
#         a1 += 1
#     if bone1 == 2:
#         a2 += 2
#     if bone1 == 3:
#         a3 += 3
#     if bone1 == 4:
#         a4 += 4
#     if bone1 == 5:
#         a5 += 5
#     if bone1 == 6:
#         a6 += 6
#
#     if bone2 == 1:
#         b1 += 1
#     if bone2 == 2:
#         b2 += 2
#     if bone2 == 3:
#         b3 += 3
#     if bone2 == 4:
#         b4 += 4
#     if bone2 == 5:
#         b5 += 5
#     if bone2 == 6:
#         b6 += 6
# print("Первая кость:"+"1-"+str(a1)+" раз,"+"2-"+str(a2//2)+" раз,"+"3-"+str(a3//3)+" раз,"+"4-"+str(a4//4)+" раз,"
#       + "5-"+str(a5//5)+" раз,"+"6-"+str(a6//6)+" раз.")
# print("Вторая кость:"+"1-"+str(b1)+" раз,"+"2-"+str(b2//2)+" раз,"+"3-"+str(b3//3)+" раз,"+"4-"+str(b4//4)+" раз,"
#       + "5-"+str(b5//5)+" раз,"+"6-"+str(b6//6)+" раз.")



