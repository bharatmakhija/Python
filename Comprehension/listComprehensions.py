a = [1,2,3,4,5]
squares = [x ** 2 for x in a]
print(squares)

squares_using_map = map(lambda x:x **2, a)
print(list(squares_using_map))

# filter all even squares

even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)

even_squares_using_map = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
print(list(even_squares_using_map))