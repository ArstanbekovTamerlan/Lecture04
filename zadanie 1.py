import random

while True:
    try:
        N = int(input("Введите нужное количество элементов массива: "))
        break
    except (TypeError, ValueError) as e:
        print("Что-то сломалось, введите целое число!", e)

res = []
for x in range(0, N):
    res=random.sample(range(0,1000),N)
print(*res)