# basic_flask_template
Simple flask server for display static image results

## Setup

Can use this is a starting guide.
https://flask.palletsprojects.com/en/1.1.x/quickstart/

Need to export the name of the controller script.
```
export FLASK_APP=app.py
```

To run the app on a vm on port 8000:
```
flask run --host=0.0.0.0 --port=8000
```

Make sure to open up the port on the VM.

## Authentication

You can probably leave everything the same of logging in within app.py except:

Can change the list of users.
```
users = [User("sohrab"),User("tyler"),User("nick"),User("ignacio"),User("hongyu"),User("maryam"),User("andrew"),User("kieran")]
```

Can change how the pass word is constructed for a user.
```
class User(UserMixin):

    def __init__(self, user):
        self.id = id
        self.name = user
        self.password = user + "_spectrum"

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)
```

Can change password validation:
```
        username = request.form['username']
        password = request.form['password']
        if password == username + "_spectrum":
```

## App page routing

Decorate any functions with "@login_required" to keep protected.

Change the landing page here:
```
@app.route('/')
@login_required
def index():
    return render_template('index.html')
```

All_samples function returns meta data from a csv and feeds it as a list of dictionaries to the jinja template "sample.html".
```
@app.route('/sample')
@login_required
def sample():
    samples = all_samples()
    table = []
    for sample_id, data in samples.items():
        table.append(data)
    return render_template('sample.html',table=table)
```
It pulls it from a google sheet, can probably refactor this code to use your own google sheet or just load a dictionary of sample to metadata.  Check sample.html template code i.e. {{}} to see how you can provide paths to static images within "static" directory and show them.

## Thumbnail / Carousel JS code

You can probably just trash this and show each figure at full size if you need to get it up faster.  Otherwise, you need to pre generate smaller thumbnail images.
























