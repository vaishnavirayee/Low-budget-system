from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def log_uid(uid):
    conn = sqlite3.connect('dispatch.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO dispatch_log (uid) VALUES (?)", (uid,))
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('dispatch.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM dispatch_log")
    rows = cur.fetchall()
    return render_template('index.html', logs=rows)

@app.route('/log', methods=['POST'])
def log():
    uid = request.form['uid']
    log_uid(uid)
    return 'Logged UID: ' + uid

if __name__ == '__main__':
    app.run(debug=True)
