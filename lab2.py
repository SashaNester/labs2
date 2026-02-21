from flask import Blueprint, url_for, request, redirect, make_response, abort, render_template
import datetime
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2/lab2.html')


@lab2.route('/lab2/a')
def a():
    return 'без слэша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']


@lab2.route('/lab2/add_flower')
def add_flower_without_name():
    return make_response("Вы не задали имя цветка", 400)


@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list) or flower_id < 0:
        abort(404)
    else:
        return render_template(
            'lab2/flower_simple.html',
            flower_id=flower_id,
            flower_name=flower_list[flower_id],
            flower_number=flower_id + 1,
            total_flowers=len(flower_list)
        )


@lab2.route('/lab2/add_flower/<name>')
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


@lab2.route('/lab2/all_flowers')
def all_flowers():
    numbered_list = ""
    for i, flower in enumerate(flower_list, 1):
        numbered_list += f"{i}. {flower}<br>"
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Все цветы</h1>
        <p>Количество цветов: {len(flower_list)}</p>
        <h2>Список цветов:</h2>
        {numbered_list}
    </body>
</html>
'''


@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Коллекция цветов очищена</h1>
        <p>Все цветы были удалены.</p>
        <p>Текущее количество цветов: {len(flower_list)}</p>
        <br>
        <a href="/lab2/all_flowers">К списку цветов</a>
    </body>
</html>
'''


@lab2.route('/lab2/example')
def example():
    name = 'Александра Нестерова'
    number = 2
    group = 'ФБИ-32'
    course = 3
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('lab2/example.html', name=name, number=number, group=group, course=course, fruits=fruits)


@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase = phrase)


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    add_res = a + b 
    sub_res = a - b 
    mul_res = a * b 
    div_res = None if b == 0 else a / b 
    pow_res = a ** b 

    div_text = 'делить на 0 нельзя &#9940;' if div_res is None else f'{div_res}'
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Расчет с параметрами:</h1>
        <div>
            {a} + {b} = {add_res} <br>
            {a} - {b} = {sub_res} <br>
            {a} × {b} = {mul_res} <br>
            {a} / {b} = {div_text} <br>
            {a}<sup>{b}</sup> = {pow_res} <br>
        </div>
    </body>
</html>
'''


@lab2.route('/lab2/calc/')
def calc_default():
    return redirect(url_for('lab2.calc', a=1, b=1))


@lab2.route('/lab2/calc/<int:a>')
def calc_one_param(a):
    return redirect(url_for('lab2.calc', a=a, b=1))


books = [
    {'author': 'Фёдор Достоевский', 'title': 'Преступление и наказание', 'genre': 'Роман', 'pages': 672},
    {'author': 'Лев Толстой', 'title': 'Война и мир', 'genre': 'Роман-эпопея', 'pages': 1300},
    {'author': 'Михаил Булгаков', 'title': 'Мастер и Маргарита', 'genre': 'Роман', 'pages': 480},
    {'author': 'Джордж Оруэлл', 'title': '1984', 'genre': 'Антиутопия', 'pages': 328},
    {'author': 'Антуан де Сент-Экзюпери', 'title': 'Маленький принц', 'genre': 'Сказка', 'pages': 96},
    {'author': 'Джейн Остин', 'title': 'Гордость и предубеждение', 'genre': 'Роман', 'pages': 416},
    {'author': 'Эрих Мария Ремарк', 'title': 'Три товарища', 'genre': 'Роман', 'pages': 384},
    {'author': 'Александр Пушкин', 'title': 'Евгений Онегин', 'genre': 'Роман в стихах', 'pages': 224},
    {'author': 'Николай Гоголь', 'title': 'Мёртвые души', 'genre': 'Поэма', 'pages': 352},
    {'author': 'Рэй Брэдбери', 'title': '451 градус по Фаренгейту', 'genre': 'Антиутопия', 'pages': 256},
    {'author': 'Габриэль Гарсиа Маркес', 'title': 'Сто лет одиночества', 'genre': 'Магический реализм', 'pages': 544}
]


@lab2.route('/lab2/books_list')
def books_list():
    return render_template('lab2/books.html', books=books)


berries = [
    {'name': 'Клубника', 'description': 'Сладкая и ароматная ягода', 'image': 'клубника.jpg', 'season': 'Июнь-Июль'},
    {'name': 'Малина', 'description': 'Нежная ягода с уникальным вкусом', 'image': 'малина.jpg', 'season': 'Июль-Август'},
    {'name': 'Черника', 'description': 'Полезна для зрения', 'image': 'черника.jpg', 'season': 'Июль-Сентябрь'},
    {'name': 'Клюква', 'description': 'Кислая ягода для морсов', 'image': 'клюква.jpg', 'season': 'Сентябрь-Октябрь'},
    {'name': 'Ежевика', 'description': 'Чёрная сладкая ягода', 'image': 'ежевика.jpg', 'season': 'Август-Сентябрь'},
    {'name': 'Брусника', 'description': 'Северная ягода', 'image': 'брусника.jpg', 'season': 'Август-Октябрь'},
    {'name': 'Смородина красная', 'description': 'Красная ягода', 'image': 'крассмор.jpg', 'season': 'Июль-Август'},
    {'name': 'Смородина чёрная', 'description': 'Ароматная чёрная ягода', 'image': 'черсмор.jpg', 'season': 'Июль-Август'},
    {'name': 'Крыжовник', 'description': 'Прозрачная ягода', 'image': 'крыжовник.jpg', 'season': 'Июль-Август'},
    {'name': 'Земляника', 'description': 'Лесная ягода', 'image': 'земляника.jpg', 'season': 'Июнь-Июль'},
    {'name': 'Голубика', 'description': 'Крупная синяя ягода', 'image': 'голубика.jpg', 'season': 'Июль-Август'},
    {'name': 'Морошка', 'description': 'Янтарная северная ягода', 'image': 'морошка.jpg', 'season': 'Июль-Август'},
    {'name': 'Калина', 'description': 'Красная горькая ягода', 'image': 'калина.jpg', 'season': 'Сентябрь-Октябрь'},
    {'name': 'Рябина', 'description': 'Оранжево-красные ягоды', 'image': 'рябина.jpg', 'season': 'Сентябрь-Ноябрь'},
    {'name': 'Шиповник', 'description': 'Дикая роза', 'image': 'шиповник.jpg', 'season': 'Август-Октябрь'},
    {'name': 'Облепиха', 'description': 'Оранжевая ягода', 'image': 'облепиха.jpg', 'season': 'Август-Сентябрь'},
    {'name': 'Виноград', 'description': 'Сладкие ягоды гроздьями', 'image': 'виноград.jpg', 'season': 'Август-Октябрь'},
    {'name': 'Барбарис', 'description': 'Красные кислые ягоды', 'image': 'барбарис.jpg', 'season': 'Сентябрь-Октябрь'},
    {'name': 'Арбуз', 'description': 'Самая большая ягода', 'image': 'арбуз.jpg', 'season': 'Июль-Август'},
    {'name': 'Жимолость', 'description': 'Синие ягоды', 'image': 'жимолость.jpg', 'season': 'Июнь'}
]


@lab2.route('/lab2/berries_list')
def berries_list():
    return render_template('lab2/berries.html', berries=berries)
