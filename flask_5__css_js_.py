# Flask #4: Функция url_for и переменные URL-адреса
from flask import Flask, render_template, url_for, request

# Функция url_for - позволяет подключать css, js, должно фигурировать имя функции обработчика
# url_for('static', filename='css/styles.css') - зарезервирован специальный параметр 'static', означает, что
# нужно обратиться к подкаталогу static и там взять файл, указанный в именованном параметре filename
app = Flask(__name__)

# Для отображения меню как ссылки прописываем список из словарей: ключ-name:название меню, ключ-url:соответствующий адресс url
menu = [{"name": "Downloading", "url": "install-flask"},
        {"name": "First application", "url": "first-app"},
        {"name": "Feedback", "url": "contact"}]

# с помощью декоратора .route() мы можем создавать привязку функции к определенному url адрессу
@app.route("/")
def index():
    return render_template('index.html', menu=menu)

@app.route("/about")
def about():
    return render_template('about.html', title="About website", menu=menu)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    # Проверка запроса 'POST' - ImmutableMultiDict([('username', ''), ('email', ''), ('message', '')])
    # ImmutableMultiDict([('username', 'Yurii'), ('email', 'autocadmdav@gmail.com'), ('message', 'Hello Flask!')])
    # Можно брать данные на сервере, которые передал пользователь через форму и что-то дальше с ними делать
    if request.method == 'POST':
        print(request.form)
        # например нужно взять только username, обратимся к нему по ключу
        print(request.form['username'])

    return render_template('contact.html', title="Feedback", menu = menu)

# webserver start
if __name__ == "__main__":
    app.run(debug=True)

# как мне сделать чтобы я вернул клиенту обработанные данные?
# Когда функция представления возвращает данные , например, return "<h1>Про Flask</h1>", то это и уходит клиенту.