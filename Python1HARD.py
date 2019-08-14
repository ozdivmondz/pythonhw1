# Задача 1 СЛОЖНАЯ
Name = input('Enter you\'r name')
age = int(input('Enter you\'r age:  '))
weight = int(input('Enter you\'r weight:  '))

if int(age) <= 30 and 120 >= int(weight) >= 50:
    print(Name, age, 'Years old', 'weight is', weight, 'Good health! keep it up :)')
elif int(age) >= 30 and 120 <= int(weight) <= 50:
    print(Name, age, 'Years old', 'Weight is', weight, 'You should do some sports and keep yourself in good health')
elif int(age) >= 40 and 150 <= int(weight) <= 50:
    print(Name, age, 'Years old', 'Weight is', weight, 'You should go to the doctor as soon as possible!')

