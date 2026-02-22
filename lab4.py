from flask import Blueprint, request, render_template, redirect, session
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнени!')

    x1 = int(x1)
    x2 = int(x2)

    if x2 == 0:
        return render_template('lab4/div.html', error='На ноль делить нельзя!')

    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')


@lab4.route('/lab4/sum', methods = ['POST'])
def sum():
    x1 = request.form.get('x1', '')
    x2 = request.form.get('x2', '')
    
    num1 = int(x1) if x1 != '' else 0
    num2 = int(x2) if x2 != '' else 0
    result = num1 + num2
    
    return render_template('lab4/sum.html', x1=num1, x2=num2, result=result)


@lab4.route('/lab4/mul-form')
def mul_form():
    return render_template('lab4/mul-form.html')


@lab4.route('/lab4/mul', methods=['POST'])
def mul():
    x1 = request.form.get('x1', '')
    x2 = request.form.get('x2', '')
    
    num1 = int(x1) if x1 != '' else 1
    num2 = int(x2) if x2 != '' else 1
    result = num1 * num2
    
    return render_template('lab4/mul.html', x1=num1, x2=num2, result=result)


@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')


@lab4.route('/lab4/sub', methods = ['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', error='Оба поля должны быть заполнены!')

    x1 = int(x1)
    x2 = int(x2)

    result = x1 - x2
    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/pow-form')
def pow_form():
    return render_template('lab4/pow-form.html')


@lab4.route('/lab4/pow', methods = ['POST'])
def pow():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/pow.html', error='Оба поля должны быть заполнены!')

    x1 = int(x1)
    x2 = int(x2)

    if x1 == 0 and x2 == 0:
        return render_template('lab4/pow.html', error='Оба поля не могут быть равны 0!')

    result = x1 ** x2
    return render_template('lab4/pow.html', x1=x1, x2=x2, result=result)


tree_count = 0

@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)

    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        if tree_count < 8:
            tree_count += 1

    return redirect('/lab4/tree')


users = [
    {'login': 'alex', 'password': '123', 'name': 'Alex', 'sex': 'мужской'},
    {'login': 'bob', 'password': '555', 'name': 'Bob', 'sex': 'мужской'},
    {'login': 'sasha', 'password': '888', 'name': 'Александра', 'sex': 'женский'},
    {'login': 'masha', 'password': '321', 'name': 'Мария', 'sex': 'женский'},
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            for user in users:
                if user['login'] == session['login']:
                    return render_template('lab4/login.html', authorized=True, name=user['name'])
            session.pop('login', None)
        
        return render_template('lab4/login.html', authorized=False, login='')
    
    login = request.form.get('login', '')
    password = request.form.get('password', '')
    error = None
    
    if login == '':
        error = 'Не введён логин'
    elif password == '':
        error = 'Не введён пароль'
    else:
        for user in users:
            if login == user['login'] and password == user['password']:
                session['login'] = login
                return redirect('/lab4/login')
        
        error = 'Неверные логин и/или пароль'
    
    return render_template('lab4/login.html', authorized=False, login=login, error=error)


@lab4.route('/lab4/logout', methods = ['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/fridge-form')
def fridge_form():
    return render_template('lab4/fridge-form.html')

@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return redirect(url_for('lab4.fridge_form'))
    
    temperature = request.form.get('temperature')
    error = None
    result = None
    snowflakes = 0
    
    if temperature == '' or temperature is None:
        error = 'Ошибка: не задана температура'
    else:
        try:
            temp = int(temperature)
            
            if temp < -12:
                error = 'Не удалось установить температуру — слишком низкое значение'
            elif temp > -1:
                error = 'Не удалось установить температуру — слишком высокое значение'
            elif -12 <= temp <= -9:
                result = f'Установлена температура: {temp}°С'
                snowflakes = 3
            elif -8 <= temp <= -5:
                result = f'Установлена температура: {temp}°С'
                snowflakes = 2
            elif -4 <= temp <= -1:
                result = f'Установлена температура: {temp}°С'
                snowflakes = 1
                
        except ValueError:
            error = 'Ошибка: введите корректное целое число'
    
    return render_template('lab4/fridge.html', 
                         error=error, 
                         result=result, 
                         snowflakes=snowflakes,
                         temperature=temperature)