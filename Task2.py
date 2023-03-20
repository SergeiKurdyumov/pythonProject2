x = int(input('Введите сумму чисел'))
y = int(input('Введите произведение чисел'))
if x and y < 2001:
    for i in range(x):
        for j in range(y):
            if x == i + j and y == i * j:
                print(i, j)
else:
    print("Задуманные числа больше 1000, попробуйте снова")

