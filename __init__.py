from flask import Flask, render_template
from flask.ext.pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_DBNAME"] = "cats"
app.config["MONGO_HOST"] = "linus.mongohq.com"
app.config["MONGO_PORT"] = 10042
app.config["MONGO_USERNAME"] = "hello"
app.config["MONGO_PASSWORD"] = "world"
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('ratemycat.html')

@app.route('/submit')
def submit():
    post = {"author": "Mike", "title": "Cat", "text": "here is my awesome cat"
            }
    posts = mongo.db.posts
    post_id = posts.insert(post)
    return render_template('ratemycat.html', post=post)

@app.route('/cat')
def cat():
    post = {"author": "Mike", "title": "Cat", "text": "here is my awesome cat"}
    posts = mongo.db.posts
    post_id = posts.insert(post)
    return render_template('ratemycat.html', post=post)

app.debug = True

if __name__ == '__main__':
    app.run()