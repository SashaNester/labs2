from flask import Blueprint, url_for, request, redirect, make_response, abort
import datetime
lab1 = Blueprint('lab1', __name__)


@lab1.route("/lab1")
def lab():
    return """<!doctype html>
<html>
    <head>
        <title>Лабораторная 1</title>
    </head>
    <body>
        <h1>Лабораторная работа 1</h1>
        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые ба-
            зовые возможности.
        </p>
        <a href="/">Вернуться на главную</a>

        <h2>Список роутов</h2>
        <ul>
            <li><a href="/lab1/web">Web-сервер на Flask</a></li>
            <li><a href="/lab1/author">Информация об авторе (author)</a></li>
            <li><a href="/lab1/info">Информация об авторе (info)</a></li>
            <li><a href="/lab1/image">Изображение дуба</a></li>
            <li><a href="/lab1/counter">Счётчик посещений</a></li>
            <li><a href="/lab1/clear_counter">Очистка счётчика</a></li>
            <li><a href="/lab1/created">Страница с кодом 201 (Created)</a></li>
            <li><a href="/error400">Ошибка 400 (Bad Request)</a></li>
            <li><a href="/error401">Ошибка 401 (Unauthorized)</a></li>
            <li><a href="/error402">Ошибка 402 (Payment Required)</a></li>
            <li><a href="/error403">Ошибка 403 (Forbidden)</a></li>
            <li><a href="/error405">Ошибка 405 (Method Not Allowed)</a></li>
            <li><a href="/error418">Ошибка 418 (I'm a teapot)</a></li>
            <li><a href="/error500">Ошибка 500 (Internal Server Error)</a></li>
        </ul>
    </body>
</html>"""


@lab1.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
            <body>
                <h1>web-сервер на flask</h1>
                <a href="/lab1/author">author</a>
            </body>
        </html>""", 200, {
            "X-Server": "sample",
            "Content-Type": "text/html; charset=utf-8"
            }


@lab1.route("/lab1/author")
def author():
    name = " Нестерова Александра"
    group = "ФБИ-32"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1/web">web</a>
            </body>
        </html>"""


@lab1.route('/lab1/image')
def image():
    path = url_for("static", filename="lab1/oak.jpg")
    css_path = url_for("static", filename="lab1/lab1.css")
    
    html_content = '''
<!doctype html>
<html>
    <body class=a>
        <h1>Дуб</h1>
        <img src="''' + path + '''">
        <link rel="stylesheet" href="''' + css_path + '''">
    </body>
</html>
'''
    
    response = make_response(html_content)
    
    response.headers['Content-Language'] = 'ru'
    
    response.headers['X-Image-Type'] = 'Nature'
    response.headers['X-Author'] = 'Nesterova_Alexandra'
    
    return response

count = 0


@lab1.route('/lab1/counter')
def counter():
    global count
    count += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз заходили сюда: ''' + str(count) + '''
        <hr>
        Дата и время: ''' + str(time) + '''<br>
        Запрошенный адрес: ''' + str(url) + '''<br>
        Ваш IP-адрес: ''' + str(client_ip) + '''<br>
        <hr>
        <a href="''' + url_for('lab1.clear_counter') + '''">Очистить счётчик</a>
    </body>
</html>
'''


@lab1.route('/lab1/clear_counter')
def clear_counter():
    global count
    count = 0
    return '''
<!doctype html>
<html>
    <body>
        <h2>Счётчик очищен!</h2>
        <p>Текущее значение: 0</p>
        <a href="''' + url_for('lab1.counter') + '''">Вернуться к счётчику</a>
    </body>
</html>
'''


@lab1.route("/lab1/info")
def info():
    return redirect("/lab1/author")


@lab1.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201


@lab1.route("/error400")
def error400():
    return make_response("400 Bad Request — Некорректный запрос", 400)


@lab1.route("/error401")
def error401():
    return make_response("401 Unauthorized — Не авторизован", 401)


@lab1.route("/error402")
def error402():
    return make_response("402 Payment Required — Требуется оплата", 402)


@lab1.route("/error403")
def error403():
    return make_response("403 Forbidden — Доступ запрещён", 403)


@lab1.route("/error405")
def error405():
    return make_response("405 Method Not Allowed — Метод не разрешён", 405)


@lab1.route("/error418")
def error418():
    return make_response("418 I'm a teapot — Я — чайник", 418)


@lab1.route("/error500")
def error500():
    try:
        result = 10 / 0
        return "Эта строка не будет показана"
    except:
        abort(500)