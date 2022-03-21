from flask import Flask, render_template        # render_template - это Jinja 2

app = Flask(__name__)

# Создание списка menu
menu = ["Downloading", "First application", "Feedback"]

@app.route("/index")

@app.route("/")
def index():
    return render_template('index.html', menu=menu)
    # return render_template('index_base.html', title = "Main page - about FLask", menu=menu)
                                         # Jinja2 - указываем какой шаблон нужно брать. Теперь файл, загружается, обрабатывается и отдается браузеру
     # return '''index'''                # ''' ''' - использование многострочных строк. Все html шаблоны хранятся в виде
                                         # отдельных файлов и загружаются по мере необходимости. Jinga2 - шаблонизатор html

@app.route("/about")
def about():
    return render_template('about.html', title = "About website", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)

    # Благодаря раширению базового шаблона у нас теперь нет дублирования базовых шаблонов
    # можем создавать теперь множество страниц сайта и при необходимости меняя структуру, меняя шаблон base.html