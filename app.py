from flask import Flask, url_for, request, redirect, make_response, abort, render_template
import datetime
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return """<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        </header>
        
        <nav>
            <ul>
                <li><a href="/lab1">Первая лабораторная</a></li>
            </ul>
        </nav>
        
        <footer>
            <hr>
            <p>Нестерова Александра, ФБИ-32, 3 курс, 2025</p>
        </footer>
    </body>
</html>"""



@app.errorhandler(404)
def not_found(err):
    error_image = url_for("static", filename="404.png")
    return f'''
<!doctype html>
<html>
    <head>
        <title>404 - Страница не найдена</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                color: white;
            }}
            .error-container {{
                text-align: center;
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                max-width: 500px;
            }}
            .error-image {{
                width: 200px;
                height: 200px;
                margin-bottom: 20px;
                border-radius: 50%;
                object-fit: cover;
            }}
            .error-code {{
                font-size: 72px;
                font-weight: bold;
                margin: 0;
                color: #ff6b6b;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }}
            .error-title {{
                font-size: 24px;
                margin: 10px 0;
                color: #ffeaa7;
            }}
            .error-message {{
                font-size: 16px;
                margin: 20px 0;
                line-height: 1.6;
            }}
            .home-button {{
                display: inline-block;
                padding: 12px 30px;
                background: #ff6b6b;
                color: white;
                text-decoration: none;
                border-radius: 25px;
                font-weight: bold;
                transition: all 0.3s ease;
                margin-top: 20px;
            }}
            .home-button:hover {{
                background: #ff5252;
                box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4);
            }}
            .search-tip {{
                background: rgba(255, 255, 255, 0.2);
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <div class="error-container">
            <img src="{error_image}" alt="Ошибка 404" class="error-image">
            <h2 class="error-title">Ой! Страница потерялась в цифровом пространстве</h2>
            
            <div class="error-message">
                <p>Кажется, эта страница отправилась в незапланированный отпуск 🏖️</p>
                <p>Возможно, она путешествует по серверам или просто решила спрятаться от нас!</p>
            </div>
            
            <div class="search-tip">
                <strong>Что можно сделать:</strong><br>
                - Проверьте адрес на опечатки<br>
                - Вернитесь на главную страницу<br>
                - Используйте меню навигации<br>
                - Просто наслаждайтесь этой красивой страницей ошибки
            </div>
            
            <a href="/" class="home-button">Вернуться на главную</a>
        </div>
    </body>
</html>
''', 404

@app.route("/lab1")
def lab1():
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

@app.route("/lab1/web")
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

@app.route("/lab1/author")
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

@app.route('/lab1/image')
def image():
    path = url_for("static", filename="oak.jpg")
    css_path = url_for("static", filename="lab1.css")
    
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

@app.route('/lab1/counter')
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
        <a href="''' + url_for('clear_counter') + '''">Очистить счётчик</a>
    </body>
</html>
'''

@app.route('/lab1/clear_counter')
def clear_counter():
    global count
    count = 0
    return '''
<!doctype html>
<html>
    <body>
        <h2>Счётчик очищен!</h2>
        <p>Текущее значение: 0</p>
        <a href="''' + url_for('counter') + '''">Вернуться к счётчику</a>
    </body>
</html>
'''

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
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

@app.route("/error400")
def error400():
    return make_response("400 Bad Request — Некорректный запрос", 400)


@app.route("/error401")
def error401():
    return make_response("401 Unauthorized — Не авторизован", 401)


@app.route("/error402")
def error402():
    return make_response("402 Payment Required — Требуется оплата", 402)


@app.route("/error403")
def error403():
    return make_response("403 Forbidden — Доступ запрещён", 403)


@app.route("/error405")
def error405():
    return make_response("405 Method Not Allowed — Метод не разрешён", 405)


@app.route("/error418")
def error418():
    return make_response("418 I'm a teapot — Я — чайник", 418)


@app.route("/error500")
def error500():
    result = 10 / 0
    return "Эта строка не будет показана"


@app.errorhandler(500)
def internal_server_error(err):
    return f'''
<!doctype html>
<html>
    <head>
        <title>500 - Ошибка сервера</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                color: white;
            }}
            .error-container {{
                text-align: center;
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                max-width: 600px;
                width: 90%;
            }}
            .error-code {{
                font-size: 100px;
                font-weight: bold;
                margin: 0;
                color: #ffeaa7;
                text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.4);
            }}
            .error-title {{
                font-size: 32px;
                margin: 20px 0;
                color: #ffeaa7;
            }}
            .error-message {{
                font-size: 18px;
                margin: 30px 0;
                line-height: 1.8;
                background: rgba(255, 255, 255, 0.15);
                padding: 20px;
                border-radius: 15px;
            }}
            .home-button {{
                display: inline-block;
                padding: 12px 30px;
                background: #ffeaa7;
                color: #ff6b6b;
                text-decoration: none;
                border-radius: 25px;
                font-weight: bold;
                transition: all 0.3s ease;
                margin-top: 20px;
                border: none;
                cursor: pointer;
            }}
            .home-button:hover {{
                background: #fdcb6e;
                box-shadow: 0 5px 15px rgba(253, 203, 110, 0.4);
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <div class="error-container">
            
            <h1 class="error-code">500</h1>
            <h2 class="error-title">Внутренняя ошибка сервера</h2>
            
            <div class="error-message">
                <p><strong>Упс! Что-то пошло не так на нашей стороне.</strong></p>
                <p>Сервер столкнулся с непредвиденной ошибкой при обработке вашего запроса.</p>
                <p>Наши разработчики уже уведомлены и работают над решением проблемы.</p>
            </div>
            
            <a href="/" class="home-button">Вернуться на главную</a>
        </div>
    </body>
</html>
''', 500

@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        abort(404)
    else:
        return "цветок: " + flower_list[flower_id]

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Александра Нестерова'
    number = 2
    group = 'ФБИ-32'
    course = 3
    return render_template('example.html', name=name, number=number, group=group, course=course)