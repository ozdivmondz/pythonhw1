#Задача 1

Correct = False
while not Correct:
    i = int(input('Enter a number, it has to be more than 0 and less than 10'))
    if i > 0 and i < 10:
        print(i ** 2)
        Correct = True
    else:
        print('Not a correct number!')
        continue

#Задача 2
i = input('Enter a number')

j = input('Enter another number')

i,j = j,i


print(i,j)
