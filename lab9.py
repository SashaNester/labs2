from flask import Blueprint, render_template, session, request, jsonify
import random

lab9 = Blueprint("lab9", __name__, template_folder="templates")

GIFTS = []

MESSAGES = [
    "Удачи!",
    "Счастья!",
    "Успехов!",
    "Радости!",
    "Тепла!",
    "Вдохновения!",
    "Мира!",
    "Добра!",
    "Любви!",
    "Света!"
]


def init_gifts():
    global GIFTS

    if GIFTS:
        return

    for i in range(10):
        GIFTS.append({
            "id": i,
            "opened": False,
            "top": random.randint(5, 80),
            "left": random.randint(5, 80),
            "box": f"box{i+1}.png",
            "gift": f"gift{i+1}.png",
            "message": MESSAGES[i]
        })


@lab9.route("/lab9/")
def index():
    init_gifts()

    return render_template(
        "lab9/index.html",
        gifts=GIFTS,
        opened=session.get("opened", 0),
        remaining=sum(not g["opened"] for g in GIFTS)
    )


@lab9.route("/open", methods=["POST"])
def open_gift():
    data = request.json
    gift_id = data.get("id")

    if gift_id is None:
        return jsonify({"error": "Некорректный запрос"})

    gift = GIFTS[gift_id]

    if gift["opened"]:
        return jsonify({"error": "Этот подарок уже открыт"})

    if session.get("opened", 0) >= 3:
        return jsonify({"error": "Можно открыть не более 3 подарков"})

    gift["opened"] = True
    session["opened"] = session.get("opened", 0) + 1

    return jsonify({
        "ok": True,
        "message": gift["message"],
        "image": gift["gift"],
        "opened": session["opened"],
        "remaining": sum(not g["opened"] for g in GIFTS)
    })