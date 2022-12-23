
# C помощью Flask запустим http сервер, напишем API, подёргаем эндпоинты
# для начала установим:  pip install virtualenv
# далее создадим папку через терминал:  virtualenv venv
#
from flask import Flask, request, jsonify
#создадим переменную, которую будем использовать, когда дёргать эндпоинты
app = Flask(__name__)

@app.route("/yolochka")
def yolochka_1():
    return "The first flask page. S novim godom"
# Надо запустить виртуальное окружение, в котором будет интерпретатор Python. И перейдя в окружение
#  установлю: pip install flask
#  правильно запустим API
#активируем папку виртуальную: source/Scripts/activate  Для деактивации: deactivate
# делаем экспорт переменных: export FLASK_APP="flask_run.py" (название файла, откуда стартанём сервак)
#запустим теперь: flask run --host="0.0.0.0" --port="5077"      Далее будет ссылка, жмём на неё и подставляем эндпоинты

# для выключения сервака: Ctrl + C , какие-то изменения - снова делаем запуск flask
@app.route("/test_method_get", methods= ["GET"])
def yolochka_2():
    p1 = int(request.args.get('salary'))
    p2 = request.args.get('name')
    resp = {'name': p2,
            'salary': p1*5}
    return jsonify(resp)

@app.route("/method_post", methods= ['GET', 'POST'])
def yolochka_3():
    if request.method == 'POST':
        p1 = int(request.form.get('salary'))
        p2 = request.form.get('name')
        resp = {'name': p2,
                'salary': p1 * 5}
        return jsonify(resp)
    elif request.method == 'GET':
        return 'HEllo'
@app.route("/yo", methods=["YO"])
def yolochka_4():
    return 'Vse budet horosho!!!!!!!!!!!!'