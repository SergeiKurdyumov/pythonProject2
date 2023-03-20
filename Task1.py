n = int(input('Введите число монет на столе'))
EagleSide = 0
TailsSide = 0
print('вводите поочерёдно монеты определяя как они лежат, где 0 = решка, а 1 = орёл')
for i in range(n):
    y = int(input())
    if y == 0:
        EagleSide += 1
    else:
        TailsSide += 1
if EagleSide > TailsSide:
    print(TailsSide)
else:
     print(EagleSide)
