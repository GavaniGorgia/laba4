from flask import Flask, render_template, redirect,request
import psycopg2

app = Flask(__name__)


@app.route('/',methods=['GET'])
def ref():
   return redirect("/login/")


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def login():
    errors = "" 
    username = request.form.get('username')
    if login == "":
        errors += "введите логин,вместо пустой строки <br>"
    password = request.form.get('password')
    if password == "":
        errors += "введите пароль,вместо пустой строки <br>" 
    if errors != "" :
        return errors
    conn = psycopg2.connect(database="service",
                            user="postgres",
                            password="lolo2002",
                            host="localhost",
                            port="5432")
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users.user WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())
    print(records)
    if len(records )!=0:
        return render_template('account.html', full_name=records[0][1],login = records[0][2], password = records[0][3])
    else:
        return "Введите пароль или логин заново"