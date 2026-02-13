from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

db = [
    {"id": 1, "title": "Прибрати кімнату", "done": False},
    {"id": 2, "title": "Помити посуд", "done": False},
    {"id": 3, "title": "Перевірити пошту", "done": False},
    {"id": 4, "title": "Прочитати 10 сторінок книги", "done": False},
    {"id": 5, "title": "Прогулятися 15 хвилин", "done": False},
    {"id": 6, "title": "Написати повідомлення другу", "done": False},
]


def last_id():
    """Повертає наступний id"""
    return max(todo["id"] for todo in db) + 1 if db else 1


@app.route('/')
def home():
    return render_template('index.html', todo_list=db)


@app.route('/add', methods=['GET'])
def add_page():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def creat_task():
    title = request.form.get('title', '').strip()

    if title:
        db.append({
            "id": last_id(),
            "title": title,
            "done": False
        })

    return redirect(url_for('home'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    global db
    db = [todo for todo in db if todo["id"] != id]
    return redirect(url_for('home'))


@app.route('/update/<int:id>', methods=['POST'])
def update_task(id):
    for todo in db:
        if todo["id"] == id:
            todo["done"] = not todo["done"]
            break
    return redirect(url_for('home'))


@app.route('/stats')
def stats():
    done = sum(1 for todo in db if todo["done"])
    return render_template(
        'stats.html',
        total=len(db),
        done=done
    )


if __name__ == '__main__':
    app.run(debug=True)

