from flask import Flask, render_template, request, session, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json, secrets
from flask_mail import Mail, Message

# Load config
with open("config.json", 'r') as c:
    params = json.load(c)['params']

local_server = True
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Use a more secure way to generate secret key

# Configure SQLAlchemy
if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure Flask-Mail, we're using this to send a mail notification when someone fills out the contact form
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = params['user']
app.config['MAIL_PASSWORD'] = params['password']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# Define models
class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    sub_title = db.Column(db.String(20), unique=True, nullable=False)
    post_slug = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
    date = db.Column(db.String(10), nullable=False)


# Routes: Defining different routes where our app will redirect when an action is performed
@app.route("/")
def home():
    post = Posts.query.all()[:params['no_of_posts']]
    return render_template("index.html", params=params, post=post)


@app.route("/post/<string:p_slug>", methods=['GET'])
def new_post(p_slug):
    post = Posts.query.filter_by(post_slug=p_slug).first()
    return render_template("post.html", params=params, post=post)


@app.route("/about")
def about():
    return render_template("about.html", params=params)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
# The left one (name) is the flask variable and the right one is the variable that we fetched from the contact.html file
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(name=name, phone=phone, msg=message, date=datetime.now().strftime("%Y-%m-%d"), email=email)
        db.session.add(entry)
        db.session.commit()
        # Uncomment to enable mail sending
        # msg = Message(f'Hello, This mail is from {name}', sender=params['user'], recipients=['monishsatpuri@gmail.com'])
        # msg.body = f"Hello, the message from {name} is {message}"
        # mail.send(msg)
    # flash('This is a toast message!', 'success')
    return render_template("contact.html", params=params)


@app.route("/dashboard", methods=['GET', 'POST'])
def dash():
    if 'username' in session and session['username'] == params['admin_user']:
        post = Posts.query.all()    # this query is used to fetch all the posts from the database!
        return render_template("dashboard.html", params=params, post=post)
    if request.method == 'POST':
        username = request.form.get("email")
        userpass = request.form.get("password")
        if username == params['admin_user'] and userpass == params['admin_password']:
            session['username'] = username
            post = Posts.query.all()
            return render_template("dashboard.html", params=params, post=post)
    return render_template("login.html", params=params)


@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit_fun(sno):
    if 'username' in session and session['username'] == params['admin_user']:
        post = Posts.query.filter_by(sno=sno).first()   # used to fetch all the posts from the database according to sno
        if request.method == 'POST':
            title = request.form.get('etitle')
            subtitle = request.form.get('esubtitle')
            postslug = request.form.get('epostslug')
            content = request.form.get('econtent')
            date = datetime.now().strftime("%Y-%m-%d")

            if sno == '0':
                entry = Posts(title=title, sub_title=subtitle, post_slug=postslug, content=content, date=date)
                db.session.add(entry)
                db.session.commit()


            else:
                post.title = title
                post.sub_title = subtitle
                post.post_slug = postslug
                post.content = content
                post.date = date
                db.session.commit()
            return redirect(f"/edit/{sno}")

        return render_template("edit.html", params=params, sno=sno, post=post)
    return redirect('/dashboard')


@app.route("/delete/<string:sno>", methods=['GET', 'POST'])
def delete_fun(sno):
    if 'username' in session and session['username'] == params['admin_user']:
        post = Posts.query.filter_by(sno=sno).first()

        if post:
            db.session.delete(post)
            db.session.commit()
    return redirect('/dashboard')

# def reset_auto_increment():
#     max_sno = db.session.query(db.func.max(Posts.sno)).scalar()
#     if max_sno is None:
#         max_sno = 0
#     db.engine.execute(f"ALTER TABLE posts AUTO_INCREMENT = {max_sno + 1}")
    


@app.route("/logout")
def logout():
    session.pop('username', None)
    return render_template("login.html", params=params)

if __name__ == '__main__':
    app.run(debug=True)
