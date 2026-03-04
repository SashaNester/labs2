import os
from flask import Flask, url_for, request, redirect, make_response, abort, render_template
import datetime
from os import path
from flask_sqlalchemy import SQLAlchemy
from db import db
from db.models import users
from flask_login import LoginManager

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8

app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'aleksandra_nesterova_orm'
    db_user = 'aleksandra_nesterova_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'

else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "aleksandra_nesterova_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)

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
                <li><a href="/lab2/">Вторая лабораторная</a></li>
                <li><a href="/lab3/">Третья лабораторная</a></li>
                <li><a href="/lab4/">Четвертая лабораторная</a></li>
                <li><a href="/lab5/">Пятая лабораторная</a></li>
                <li><a href="/lab6/">Шестая лабораторная</a></li>
                <li><a href="/lab7/">Седьмая лабораторная</a></li>
                <li><a href="/lab8/">Восьмая лабораторная</a></li>
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
    error_image = url_for("static", filename="lab1/404.png")
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
