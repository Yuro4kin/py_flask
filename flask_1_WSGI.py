# остаточно для создания типовых сайтов( с поддержкой шаблонов страниц, БД)
# Flask - первое WSGI (Web Server Gateway Interface) - приложение, стандарт взаимодействия
# между Python - программой, выполняющейся на стороне сервера, и самим веб-сервером
# Напишем первое WSGI приложение в простом варианте

from flask import Flask             # импорт Flask, который формирует WSGI приложение

                                    # создадим первое WSGI приложение на FLASK
app = Flask(__name__)               # создаем экземпляр класса Flask и первым аргументом указываем имя приложения.
                                    # если программа пишется в одном файле то удобно в качестве первого аргумента передать директиву __name__
                                    # которая в случае импорта будет содержать имя текущего файла, или в случаем самостоятельного запуска значение __main__
                                    # От этого зависит где искать подкаталоги с шаблонами и статичными документами


                                    # Чтоб не было ошибки  404 нужно создать представление - декоратор route
@app.route("/index")                # На один обработчик добавляем url адрес, по которому обрабатывает данный обработчик в виде функции с именем index
                                    # / или /index - это одно и тоже. На один и тот же обработчик можем вешать сразу несколько url
@app.route("/")                     # Воспользуемся декораторм route, создадим это представление обработки запроса от клиента. В декораторе указываем url адрес по которому
def index():                        # будет отрабатывать обработчик в виде ф-ции с именем index, обработчик будет возвращать текст "index".
    return "index"                  # Браузер в ответ на адрес url главной странице ("/")  соответствует- http://127.0.0.1:5000/ - получит строку index

@app.route("/about")                # Добавим еще один обработчик, декоратор route, укажем здесь другой URL и соответствующий обработчик
def about():
    return "<h1> О сайте </h1>"     # Обработчик вернет пусть такую html страницу, перейдем на сайт и наберем http://127.0.0.1:5000/about  - браузер в ответ на адрес about получит строку с тегом h1 О сайте


if __name__ == "__main__":          # Когда запускаем наш модуль, то директива __name__ принимает значение __main__, и будет запущен локальный веб сервер для отладки нашего приложения.
    app.run(debug=True)             # После создания приложения происходит запуск локального сервера
                                    # Параметр debug=True, чтоб мы видели все ошибки которые будут возникать при разработке сайта приложения.
                                    # Параметр debug=False после создания приложения, чтоб реальные ошибки пользователь не видел.
                                    # Если модуль запускается на удаленном сервере, то нам не нужно запускать там еще один модуль Flask директива __name__ будет принимать название файла flask_1_WSGI, в котором реализована программа
                                    # В нашем случае активизируется локальный Web server и мы сможем обрабатывать и получать запросы в рамках нашего ПК
                                    # При запуске программы будет доступен  http://127.0.0.1:5000/ локальный host внутри нашего ПК, порт 5000 чтоб наш канал связи не конфликтовал с другими, которые функционируют в рамках нашего устр-ва.
                                    # Error - 127.0.0.1 - 404 -  в нагшем приложении не сформировано ни одного представления.
                                    # нет ни одного обработчика , который бы обрабатывал бы  запрос пришедший от клиента
                                    # создадим это представление обработки запроса от клиента декоратором .route

