from flask import Flask, render_template, request, redirect, url_for
from db_config import get_db_connection

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('dashboard', user=username))
    return render_template('login.html')

@app.route('/dashboard/<user>')
def dashboard(user):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM leaves")
    leaves = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', user=user, leaves=leaves)

@app.route('/apply', methods=['GET', 'POST'])
def apply_leave():
    if request.method == 'POST':
        name = request.form['name']
        reason = request.form['reason']
        days = request.form['days']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO leaves (name, reason, days, status) VALUES (%s, %s, %s, %s)",
            (name, reason, days, "Pending")
        )
        conn.commit()
        conn.close()

        return redirect(url_for('dashboard', user=name))

    return render_template('apply_leave.html')

@app.route('/update/<int:leave_id>/<string:action>')
def update_status(leave_id, action):
    status = "Approved" if action == "approve" else "Rejected"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE leaves SET status=%s WHERE id=%s",
        (status, leave_id)
    )
    conn.commit()
    conn.close()

    return redirect(request.referrer)

if __name__ == '__main__':
    app.run(debug=True)
