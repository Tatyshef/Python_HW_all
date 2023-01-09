#2. Добавить слово в конец списка так, чтобы каждая буква стала отдельным элементом списка
# l = [1, 2, 3]
# a = 'abc'
# result = [1, 2, 3, 'a', 'b', 'c']
l = [1,2,3]
a = 'abc'
# l.extend(a) #продлевает список здесь
# print(l)
for i in a:
    l.append(i)
print(l)
# 3. Все чётные числа вывести в другой список
# l = [1,3,4,5,8,9,10,44,22,50,79,54,28,91]
l = [1,3,4,5,8,9,10,44,22,50,79,54,28,91]
l_odd = []
for i in l:
    if i % 2 ==0:
        l_odd.append(i)
print('l_odd', l_odd)
# 4. Все emails у которых есть слово test вывести в другой список
l = ['webtest1@gmail.com',
     'alex_dr5@gmail.com',
     'elena_viktorovna@gmail.com',
     'infotest@gmail.com',
     'sigmatesst@gmail.com',
     'planet.dollsatest@gmail.com',
     'loadtestsinfo@gmail.com',
     'straightwaytest@gmail.com',
     'test.of.tests@gmail.com',
     'bigmac@gmail.com',
     'bigmactest@gmail.com',
     'kfc_test_supply@gmail.com',
     'cyberdesk@gmail.com',
     'supportonlinetest@gmail.com'
    ]
l_test = []
for i in l:
    if 'test' in i:
        l_test.append(i)

print('l_test', l_test)

#5.  найти самое маленькое число в списке
l = [3,0,4,5,8,9,10,44,22,50,-1,79,54,-28,91]
print('маленькое число=', min(l))

#6. Сравнить две строки без учёта регистра
s1 = 'alexander'
s2 = 'AleXandeR'

if s1.lower() == s2.lower():
    print('Равны строки')
else:
    print('Строки не равны')
# 7. Проверить является ли массив подмножеством другого массива
l1 = [1,2,6]
l2 = [9,5,1,10,4,33,2,6,0,8]
c = 0
for i in l1:
    if i in l2:
        c += 1
if c == len(l1):
    print('true')
else:
    print('false')
# 8. Напишите функцию, которая принимает строку и возвращает количество букв английского алфавита,
# которые встречаются больше чем 1 раз.
s = 'sssaaa'
abc = 'qwertyaabbcchmts'
for i in abc:
    count = 0
    for j in s:
        if j == i:
            count += 1
    if count > 1:
         print(i, 'встречается', count, 'раз')
# 9. Напишите функцию, которая принимает строки.
# Она должна вернуть False, если в строке содержится две одинаковые буквы,
# а если таких слов нет — True.
def foo(string):
    return len(set(string)) == len(string)
# print(foo("test"))
print(foo("tes"))
