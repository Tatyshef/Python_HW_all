#1. Создать пустой empty.csv файл
import csv, names, randomtimestamp as rd

path = 'D:/Python_curse/project_1/'
name = 'empty.csv'
full = path + name

with open(full, 'w') as cs:
    writer = csv.writer(cs)

# # 2. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150
path = 'D:/Python_curse/project_1/'
name = 'digits.csv'
full = path + name

with open(full, 'w', newline='') as cs:
    writer = csv.writer(cs)
    for i in range(151):
        writer.writerow([i])
# 3. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами
with open('names.csv', 'w', newline = '') as names_f:

    for i in range(100):

        name_user = names.get_full_name()
        writer = csv.writer(names_f)
        writer.writerow([name_user])

#4. Создать emals.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами что-то@gmail.com

with open('email.csv', 'w', newline = '') as email_f:

    for i in range(100):
        email_user = names.get_first_name()
        second_part = '@gmail.com'
        number =random.randint(2, 18)
        full_email = email_user + str(number) + second_part
        writer = csv.writer(email_f)
        writer.writerow([full_email])

# 5. Создать nne.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 100 строк.
# # Имя и часть email до @ должны совпадать.

with open('nne.csv', 'w') as ne_file:
    columns = ['Number', 'Name', 'Email']
    writer = csv.DictWriter(ne_file, fieldnames= columns)
    writer.writeheader()
    for i in range(100):
        name_user = names.get_full_name()
        writer.writerow({'Number': i, 'Name': name_user, 'Email': name_user.replace(' ', '_')+'@gmail.com'})

# 6.  Создать digits_2.csv файл с 1-м полем которое называется number, в котором будут
# 300 строк с числами от 10 до 310

numbers_list = list(range(10,311))
with open('digits_2.csv', 'w', newline='') as dig_file:
    column = ['Name']
    writer = csv.DictWriter(dig_file, fieldnames = column)
    writer.writeheader()
    for i in  numbers_list:
        writer.writerow({'Name': i})

# 7.  Создать names_2.csv файл с 1-м полем которое называется name, в котором будут 400 строк с разными именами

with open('names_2.csv', 'w', newline='') as names_file:
    writer = csv.DictWriter(names_file, fieldnames=['Name'])
    writer.writeheader()
    for i in range(1,401):
        user_names = names.get_full_name()
        writer.writerow({'Name': user_names})

#8.  Создать emals_2.csv файл с 1-м полем которое называется email,
# в котором будут 400 строк с разными имейлами что-то@gmail.com

with open('emails_2.csv', 'w', newline='') as email_file:
    writer = csv.DictWriter(email_file, fieldnames=['email'])
    writer.writeheader()
    for i in range(1, 401):
        name = names.get_full_name()
        writer.writerow({'email': name.replace(' ', '_') + str(i) +'@gmail.com'})
#9.Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 450 строк.
# Имя и часть email до @ должны совпадать.

with open('nne_2.csv', 'w') as name_email_file:
    writer = csv.DictWriter(name_email_file, fieldnames=['Number', 'Name', 'Email'])
    writer.writeheader()
    for i in range(1, 451):
        user_names = names.get_full_name()
        writer.writerow({'Number': i, 'Name': user_names, 'Email': user_names.replace(' ', '_') + '@gmail.com'})