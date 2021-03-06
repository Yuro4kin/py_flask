# Flask #3: Контекст приложения и контекст запроса

#                    SERVER
# Запрос 1 ---- > g, current_app         request, session
#                   контекст приложения  контекст запроса


# Запрос N ---- > g, current_app         request, session
#                   контекст приложения  контекст запроса

# g - это глобальная переменная, которая доступна в пределе контекста приложения (current_app)
# g - для сохранения пользовательской информации, необходимой для обработки запросов
# g - также в переменой g можно сохранять текущее соединение с БД, а когда запрос завершит свою работу
# закрывается соединение с переменной g и БД
# g - оработка запроса завершена, данные автоматически удаляются, т.к. данные временны в пределах существования приложения

# current_app ссылается на контекст текущего приложения, активизируется flask по зпросу
# flask - поддерживает работу сразу несколько WSGI приложений

# app1 = Flask("app1")
# app2 = Flask("app2")

# каждое приложение отвечает за свой функционал, чтобы встроенные ф-ции Flask могли работать в условиях
# нескольких приложений используется переменная current_app, которая ссылается на текущее приложение
# активизированное для соответствующего запроса

# request - содержит данные связанные с текущим запросом, часто это get() запрос (ключ:значение)
# post() - запрос при загрузке файлов

# session - это словарь в котором можно сохранять данные в пределах сессии, которая сохраняется между запросами
# session - уникальна для каждого запроса

# Например: пользователь авторизуется (логи, пароль), значения авторизации записывается в переменную session
#           теперь когда пользователь будет переходить на другие страницы сайта, мы можем брать значения
#           из данной сессии и проверять авторизовался данный пользователь или нет
#           если авторизовался мы показываем одно содержимое этих страниц, если нет то другое содержимое
# session - чтоб сохранять авторизацию текущего пользователя.
# session - связана с источником запроса, если запрос с другого источника, то там другая переменная session
#           если пользователь долго не заходил на сайт, то переменная session пропадет и пользователю опять нужно авторизоваться
# request, session - эти две переменные доступны в контексте запроса
# g, currunt_up    - эти две переменные доступны в контексте приложения