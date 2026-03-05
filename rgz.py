from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from db.models import initiative_users, initiatives
from sqlalchemy import desc

rgz = Blueprint('rgz', __name__)


@rgz.route("/rgz/")
def index():
    page = int(request.args.get("page", 1))
    per_page = 20

    initiatives_list = initiatives.query.order_by(desc(initiatives.created_at)).paginate(page=page, per_page=per_page)

    return render_template("rgz/index.html",
                           initiatives=initiatives_list.items,
                           pagination=initiatives_list)


@rgz.route("/rgz/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("rgz/register.html")

    login_form = request.form.get("login")
    password_form = request.form.get("password")

    if not login_form or not password_form:
        flash("Заполните логин и пароль", "error")
        return redirect(url_for("rgz.register"))

    if initiative_users.query.filter_by(login=login_form).first():
        flash("Такой пользователь уже есть", "error")
        return redirect(url_for("rgz.register"))

    new_user = initiative_users(
        login=login_form,
        password=generate_password_hash(password_form),
        role='user'
    )
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)
    return redirect(url_for("rgz.index"))


@rgz.route("/rgz/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("rgz/login.html")

    login_form = request.form.get("login")
    password_form = request.form.get("password")

    user = initiative_users.query.filter_by(login=login_form).first()

    if user and check_password_hash(user.password, password_form):
        login_user(user)
        return redirect(url_for("rgz.index"))

    flash("Неверный логин или пароль", "error")
    return redirect(url_for("rgz.login"))


@rgz.route("/rgz/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("rgz.index"))


@rgz.route("/rgz/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "GET":
        return render_template("rgz/create.html")

    title = request.form.get("title")
    description = request.form.get("description")

    if not title or not description:
        flash("Название и описание обязательны", "error")
        return redirect(url_for("rgz.create"))

    new_initiative = initiatives(
        user_id=current_user.id,
        title=title,
        description=description,
        votes=0
    )
    db.session.add(new_initiative)
    db.session.commit()
    return redirect(url_for("rgz.index"))


@rgz.route("/rgz/delete/<int:initiative_id>")
@login_required
def delete(initiative_id):
    initiative = initiatives.query.get_or_404(initiative_id)

    if initiative.user_id != current_user.id and current_user.role != "admin":
        flash("Нет прав на удаление", "error")
        return redirect(url_for("rgz.index"))

    db.session.delete(initiative)
    db.session.commit()
    flash("Инициатива удалена", "success")
    return redirect(url_for("rgz.index"))


@rgz.route("/rgz/vote/<int:initiative_id>/<action>")
@login_required
def vote(initiative_id, action):
    initiative = initiatives.query.get_or_404(initiative_id)

    if action == "up":
        initiative.votes += 1
    elif action == "down":
        initiative.votes -= 1

    if initiative.votes < -10:
        db.session.delete(initiative)

    db.session.commit()
    return redirect(url_for("rgz.index"))


@rgz.route("/rgz/admin/users")
@login_required
def admin_users():
    if current_user.role != "admin":
        flash("Нет доступа", "error")
        return redirect(url_for("rgz.index"))

    users_list = initiative_users.query.all()
    return render_template("rgz/admin_users.html", users=users_list)


@rgz.route("/rgz/admin/delete_user/<int:user_id>")
@login_required
def admin_delete_user(user_id):
    if current_user.role != "admin":
        flash("Нет доступа", "error")
        return redirect(url_for("rgz.index"))

    user = initiative_users.query.get_or_404(user_id)

    if user.role == "admin":
        flash("Нельзя удалить администратора", "error")
        return redirect(url_for("rgz.admin_users"))

    db.session.delete(user)
    db.session.commit()
    flash("Пользователь удален", "success")
    return redirect(url_for("rgz.admin_users"))
