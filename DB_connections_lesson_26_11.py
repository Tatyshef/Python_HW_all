import psycopg2 #библиотека для доступа к Postgres DB
#подключимся к базе

conn = psycopg2.connect(dbname = 'qa_ddl_25_139',
                        user = 'user_25_139',
                        password = '123',
                        host = '159.69.151.133',
                        port = '5056')
#достанем объект нашего коннекшена
cursor = conn.cursor()
#проверим есть ли коннекшен
if conn:
    print('Connection ok')
select_query = 'select * from public.salary;'
execute_q = cursor.execute(select_query)
get_query_result = cursor.fetchall()
# проитерируем список
for i in get_query_result:
    print(i[0], i[1])
#добавим в таблицу что-нибудь из pycharm
if conn:
    print('connection insert')
    salary = str(1234)
    insert_query = 'insert into public.salary(montly_salary)'\
    'values('+salary+')'
#сделаем исполнение строки
    cursor.execute(insert_query)
    conn.commit()
    cursor.close()
#сделаем добавление в таблицу циклом
for i in range(0,10):
    if conn:

        salary = str(9000 + i*100)
        insert_query = 'insert into public.salary(montly_salary)' \
                       'values(' + salary + ')'
        # сделаем исполнение строки
        cursor.execute(insert_query)
        conn.commit()
print('connection insert')
cursor.close()
#добавим в другую таблицу строки
for i in range(0,10):
    if conn:

        role_name = " 'Developer_" + str(i) + "'"
        insert_query = 'insert into public.roles_2(role_title)' \
                       'values(' + role_name + ')'
        print('insert_query ', insert_query)
        # сделаем исполнение строки
        cursor.execute(insert_query)
        conn.commit()
cursor.close()


