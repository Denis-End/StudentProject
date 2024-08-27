frist=int(input('Введите число: '))
second=int(input('Введите число: '))
third=int(input('Введите число: '))
if frist==second and frist==third:
    print("3")
elif second==frist:
    print("2")
elif second!=frist and frist!=third:
    print("0")