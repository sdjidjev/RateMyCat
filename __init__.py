from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "cats"
app.config["MONGO_HOST"] = "linus.mongohq.com"
app.config["MONGO_PORT"] = 10042
app.config["MONGO_USERNAME"] = "hello"
app.config["MONGO_PASSWORD"] = "world"
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('ratemycat.html')

@app.route('/submit')
def submit():
    post = {"author": "Mike", "title": "Cat", "text": "here is my awesome cat"
            }
    posts = mongo.db.posts
    post_id = posts.insert(post))
    return str(post_id)

@app.route('/cat')
def cat():
    posts = mongo.db.posts
    find = posts.find_one({"author": "Mike"})
    #LEARN TEMPLATING
if __name__ == '__main__':
    app.run()