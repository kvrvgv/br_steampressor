

catet_1 = catet_2 = ""

while True:
    catet_1 = input("Введите длину первого катета: ")
    try:
        catet_1 = int(catet_1)
    except ValueError:
        print("Ошибка: Введите длину ЧИСЛОМ")
        continue
    catet_1 = int(catet_1)
    if catet_1 <= 0:
        print("Ошибка: Длина катета должна быть НАТУРАЛЬНЫМ ЧИСЛОМ")
        continue
    break


while True:
    catet_2 = input("Введите длину второго катета: ")
    try:
        catet_2 = int(catet_2)
    except ValueError:
        print("Ошибка: Введите длину ЧИСЛОМ")
        continue
    if catet_2 <= 0:
        print("Ошибка: Длина катета должна быть НАТУРАЛЬНЫМ ЧИСЛОМ")
        continue
    break


gipotenus = (catet_1 ** 2 + catet_2 ** 2) ** 0.5

p = gipotenus + catet_2 + catet_1

s = catet_2 * catet_1 * 0.5

print(f"Площадь: {s:.2f}")
print(f"Периметр: {p:.2f}")
