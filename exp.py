# colors = {
#     "white": (255, 255, 255),
#     "grey": (128, 128, 128),
#     "red": (255, 0, 0),
#     "green": (0, 128, 0)
#     }
# for col, rgb in sorted(colors.items()):
#     print(col, ":", rgb)


# colors = (("green", "#008000"), ("blue", "#0000FF"))
# colors = [("green", "#008000"), ("blue", "#0000FF")]
# colors_dictionary = dict(colors)
# print(colors_dictionary)


# short_list = [1]
# short_list.append(2)
# short_list.depend(3)


# short_tup = (1,)
# short_tup.append(2)


# x = 92
# if x > 90
#     print("You got an 'A'!")
# SyntaxError: expected ':'


# my_list = [x*x for x in range(5)]
# print(my_list)

# lst = [[x for x in range(3)] for y in range(3)]
# print(lst)

# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")


# def func(a, b):
#     return b ** a
# print(func(b=2, 2))
# > SyntaxError: positional argument follows keyword argument

# def fun(inp=2,out=3):
#     return inp * out
# print(fun(out=2))


# lst = [i for i in range(-1, -2)]
# print(lst)



# tup = (1,2,3)
# tup.index(0)


# for v in range(2):
#     2 1 1, 2


# i = 0
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")
# > error infinite loop


# dct = {'one': 'two',
#        'three': 'one',
#        'two': 'three'}
# v = dct['three'] # 'one'
# for k in range(len(dct)):
#     v = dct[v]
# print(v)


# print(1 // 2)
# > 0


# my_list = [1,2]
# for v in range(2):
#     my_list.insert(-1, my_list[v])
# print(my_list)
# > [1, 1, 1, 2]


# x = 11
# y = 4
# print(x,y)
# x = x % y
# print(x,y)
# x = x % y
# print(x,y)
# y = y % x
# print(x,y)


# print( 1 / 2 + 3 // 3 + 4 ** 2 )
# print( 0.5 + 1 + 16 )


# x, y = 2, 4
# x = x / y
# y = y / x

# print(y)



# for i in range(-1,1):
#     print("#")



# lst = [[3,2,1],
#        [3,2,1],
#        [3,2,1]]
# s = 0
# for i in range(3):
#     0, 1, 2
#     s = s + t[i][i]
#     s = s + t[0][0] = 3
#     s = s + t[1][1] = 5
#     s = s + t[2][2] = 6



# var = 1
# while var < 10:
#     print("%")
#     var = var << 1



# i = 0
# while i <= 5:
#     i += 1
#     if i % 2 == 0:
#         break
#     print("*")



# my_list = [[0,1,2,3] for i in range(2)]
# print(my_list[2][0])

# nums = [1,2,3]
# vals = nums[-1:-2]
# print(vals)



# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
# print("#")



# my_list = [1,2,3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)



# i = 0
# while i <= 3:
#     i += 2
#     print("*")

# print(2. // -4)


# numbers = []
# for i in range(1,5):
#     numbers.insert(-2, i)
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)


# my_list = [10, 8, 6, 4, 2]
# print(my_list[:])
# print(my_list[:-1])
# print(my_list[::-1])

# board = [[i for i in range(8)] for j in range(8)]
# print(board)


# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
# introduction("James", "Bond")
# introduction("Jessie", "Owens", "Oops")



# print("hello")print("world")
# SyntaxError


# # defining the function
# customPrint(message="hello world")
# NameError
# def customPrint(message=""):
#     print("custom print said:", message)
# invoking the function
# > custom print said: hello world


# from hashlib import sha256
# a_string = "a wound healed with love"
# hashed_string = sha256(a_string.encode('utf-8')).hexdigest()
# print(hashed_string)
# "746479b0ebcfec73b26faf4bf1f276e35d4accddf3a3b40d53f370319d338252"


# convert a string to its binary representation
# > ord() function translates unicode point to its integer
# > format() function converts integer to base two using the binary format 'b'
# a_string = "love"
# b_string = ' '.join(format(ord(char), 'b') for char in a_string)
# print(b_string)


# print('asdf'*0.5)
# > TypeError

# print("hello world" * 2)
# hello worldhello world


# print(range(0))
# for i in range(0,0):
#     print(i)


# from math import pi as xyz
# print(pi)
# > NameError: no def



# lst = [[c for c in range(r)] for r in range(3)]
# print(lst)
# for x in lst:
#     print(x)
#     for y in x:
#         print(y)
#         if y < 2:
#             print('*', end='')


