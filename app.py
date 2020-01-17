from flask import Flask, Response, redirect, url_for, request, session, abort, render_template
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

from metadata import *

app = Flask(__name__)

app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx'
)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):

    def __init__(self, user):
        self.id = id
        self.name = user
        self.password = user + "_spectrum"

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

users = [User("sohrab"),User("tyler"),User("nick"),User("ignacio"),User("hongyu"),User("maryam"),User("andrew"),User("kieran")]

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == username + "_spectrum":
            id = username
            user = User(id)
            login_user(user)
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return Response('''
        <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        </head>
        <center>
        <body style="padding:20%;">
        <h1><font face="helvetica">SPECTRUM SCRNA</font></h1>

        <form action="" method="post">
          <div class="form-group">
            <label for="exampleInputEmail1">User</label>
            <input type="text" class="form-control" name=username placeholder="User">
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Password</label>
            <input type="password" class="form-control" name=password placeholder="Password">
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        <body>
        </center>
        ''')

@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

@app.route('/sample')
@login_required
def sample():
    samples = all_samples()
    table = []
    for sample_id, data in samples.items():
        table.append(data)
    return render_template('sample.html',table=table)

@app.route('/')
@login_required
def index():
    return render_template('index.html')


@login_manager.user_loader
def load_user(userid):
    return User(userid)
