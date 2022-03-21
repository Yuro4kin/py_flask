# Flask #4: Функция url_for и переменные URL-адреса
from flask import Flask, render_template, url_for

# Функция url_for - позволяет генерировать url адресс по имени функции обработчика
app = Flask(__name__)

menu = ["Установка", "Первое приложение", "Обратная связь"]

# с помощью декоратора .route() мы можем создавать привязку функции к определенному url адрессу
@app.route("/")
#@app.route("/index")   # функцию url_for() возвращает адресс, который прописан в последнем декораторе - /index
def index():
    # вызываем функцию url_for() в обработчиках главной страницы аргументом указываем ("index") - имя функции
    # в консоли мы можем видеть /, который зозвратил print() и url_for адресс главной страницы
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    # вызываем ф-цию url(for) для аргумента 'about', то возвращен url адресс /about
    # в консоли мы можем видеть /about, это url_for адресс, который связан с обработчиком 'about'
    print(url_for('about'))
    return render_template('about.html', title="О сайте", menu=menu)

# webserver start
# if __name__ == "__main__":
#     app.run(debug=True)

# функция url_for() - работает только в контексте запроса
# def index():
#     print(url_for('index'))
#     return render_template('index.html', menu=menu)

# если мы захотим вызвать функцию - print(url_for('index')) вне контекста запроса у нас возникнет ошибка
# Правило: когда приходит запрос - нужно создавать контекст запроса и внутри контекста запроса работает ф-ция, которая
# использует данные этого запроса, в данном случае url_for()

# Например нам нужно проверить ф-цию url_for() для разных обработчиков в целях тестирования
# flask позволяет нам искусственно создавать контекст запроса без активации веб сервера
# создаем тестовый контекст запроса test_request_context() внутри которого вызываем ф-цию url_for()
# на выходе получили адресс, который ассоциирован с этим значением - \ обработчиком
# with app.test_request_context():
#     print( url_for('index'))     # / или
#     print( url_for('about'))     # /'about'


# функция for будет корректно работать и при использовании нескольких WSGI приложений
# Функция url_for('about') сначала обращается к переменной current_app(контекст приложения и проверяет с
# каким из приложений ассоциирован данный запрос app1(@app.route("/about_1") или app2(@app.route("/about_2")
# для такого приложения и будет возвращен адресс, еапример /about_2

# Способы описания - url
# с помощью декоратора .route() мы можем создавать привязку функции к определенному url адрессу
# эти url адресса можно делать и переменными(динамическими)
# синтаксис:
# @app.route("/url/<variable>")
# url        - адресс
# <variable> - переменная будет принимать значение определяемое в соответсвии с url адрессом
# Например, создадим еще один обработчик. Функция обработчик profile() принимает на входе значение переменной
# username, и в браузере мы будем видеть пользователя и то, что хранится в переменной
@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"
    # http://127.0.0.1:5000/profile/pythonstartFlask
    # Пользователь: pythonstartFlask
# т.е. в нашей функции profile обработчик username значение pythonstartFlask которое мы прописали отображается на странице

# path: - username теперь принимает оставшийся путь, говорит нам, что все, что будет прописано после path будет помещено в foldername
@app.route("/myfile/<path:foldername>")
def myfile(foldername):
    return f"Пользователь: {foldername}"
    # http://127.0.0.1:5000/myfile/product/price
    # Пользователь: product/price

# Конверторы для @app.route("/url/<variable>")
# int – должны присутствовать только цифры;
# float – можно записывать число с плавающей точкой;
# path – можно использовать любые допустимые символы URL плюс символ слеша ‘/’.

# int
@app.route("/intfile/<int:integername>")
def intfile(integername):
    return f"Пользователь: {integername}"
    # http://127.0.0.1:5000/intfile/123456789
    # Пользователь: 123456789

# int, path
@app.route("/doubleconvert/<int:integername>/<path>")
def doubleconvert(integername, path):
    return f"Пользователь: {integername}, {path}"
    # http://127.0.0.1:5000/doubleconvert/123456789/textdata
    # Пользователь: 123456789, textdata




# тестовый контекст запроса и в нем вызовем url_for для разных представлений в пределах контекста:
with app.test_request_context():
    print(url_for('index'))
    print(url_for('about'))
    print(url_for('profile', username="betteredu"))
    #                        username - указать именованный параметр из динамического пути <username> и указать какое значение он должен принимать

# webserver start
# if __name__ == "__main__":
#     app.run(debug=True)