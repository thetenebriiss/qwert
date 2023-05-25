from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'zoryanasemen78@gmail.com'
app.config['MAIL_PASSWORD'] = 'rypthchccpuyzllq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/mail")
def mails():
    msg = Message('Hello',
                  sender='dear kolega',
                  recipients=['zoryanasemen78@gmail.com'])

    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/s/')
def spam():
    return render_template('spam.html', user='Stan', email='gucci@sruczi.su')


@app.route('/hello')
def hello_word():
    return 'Hello, world!'


@app.route('/hello/h1')
def hello_word_color():
    return '<h1 style="color:red">Hello, world!</h1>'


@app.route('/help')
def help():
    return 'help me'


@app.route('/contact')
def contact():
    return 'contact with me'


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/new_index')
def new_index():
    return render_template('new_index.html')


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return f'login: {request.form["username"]} <br> password: {request.form["password"]}'
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
