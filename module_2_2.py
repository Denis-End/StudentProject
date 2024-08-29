frist = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if frist == second and frist == third:
    print("3")
elif second == frist and second == third:
    print("3")
elif frist == second or second == third or third == frist:
    print("2")
else: print("0")
