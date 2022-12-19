import names, csv, random
arr = [1, 2, 3]
for i in arr:
    print(i)
#2. Сгенерить список из 20 цифр
list_1 = list(range(1, 21))
print(list_1)
#3. Сгенерить числа, которые делятся на 2 без остатка

list_3 = [i for i in range(1, 30) if i%2 != 0]
print(list_3)
#4. Сгенерить спиcок строк, где будет item_1, item_2 .... item_20
list_4 = []
for i in range(1, 21):
    sum = 'item_'+str(i)
    list_4.append(sum)
print('list_4 =', list_4)
#5. Сгенерить список из 20 имён
name_users = []
for i in range(20):
    name_1 = str(i) +  '. ' + names.get_first_name()
    name_users.append(name_1)
print(name_users)
#6. Сгенерить csv файл, где будет имя, возраст и зарплата человека. Итого: 100 строк.

with open('name_age_salary.csv', 'w') as cf:
    writer = csv.DictWriter(cf, fieldnames=['Name', 'Age', 'Salary'])
    writer.writeheader()
    for i in range(1, 101):
        name_user = names.get_full_name()
        age_user = random.randint(25, 45)
        salary_user = random.randint(23000, 45000)
        writer.writerow({'Name': name_user, 'Age': age_user, 'Salary': salary_user})

#7. Сделать список, который будет содержать внутренний список (имя, возраст, зарплату)
ls_1 = []
for i in range(20):
    ls_2 = []
    name = names.get_full_name()
    age = random.randint(22, 34)
    salary = random.randint(20000, 30000)
    ls_2.append(name)
    ls_2.append(age)
    ls_2.append(salary)
    ls_1.append(ls_2)
print(ls_1)
#8. Написать функцию, которая сгенерирует список имён, функция - возрастов.
def create_names():
    list_name = []
    for i in range(20):
        names_user = names.get_full_name()
        list_name.append(names_user)
    return list_name

name_2 = create_names()
print(name_2)


def create_age():
    list_age = []
    for i in range(20):
        age_user = random.randint(23, 45)
        list_age.append(age_user)
    return list_age
age_user = create_age()
print(age_user)


#9. Программа, которая спрашивает твоё имя. И  в ответ выдаёт 'Hello, твоё_имя'
name = input('What is your name?')
print('Hello,', name)
#для запуска программы из терминала пишем python название_файла

#10. Программа, которая спросит первую букву, спросит количество. Создать список и вывести его: внутри списка
#строка и по порядку перечисленные.
lis = []
def mix():
    a = input('введите букву: ')
    b = int(input('количество: '))

    for i in range(b):
        lis.append(a+str(i))

    return lis
print(mix())

#11. теперь, список  lis сохранить в txt файле. При чём каждый элемент с новой строки.

with open('list.txt', 'w') as tf:
    writer =tf.writelines('\n'.join(lis))
#12. Написать функцию, которая определит, высокосный год или нет

def year():
    year_1 = int(input('Введите год: '))
    if year_1 % 4 == 0:
        print('Это високосный год: ', year_1)
    else:
        print('Это невисокосный год: ',year_1)
    return year_1
year_input = year()

print(year_input)
#конец






