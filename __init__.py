from flask import Flask, render_template, request, redirect, abort
from flask.ext.pymongo import PyMongo
from bson.objectid import ObjectId

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

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        post = {"author": request.form['author'], 
        "title": request.form['title'], "text": request.form['text'], "cat":
        request.form['cat']}
        posts = mongo.db.posts
        post_id = posts.insert(post)
        return redirect('/cat/' + str(post_id))
    else:
        return render_template('submit.html')

@app.route('/cat/<post_id>')
def show_post(post_id):
    post = mongo.db.posts.find_one({"_id" :ObjectId(post_id)})
    if post is not None:
        return render_template('ratemycat.html', post=post)
    else:
        return abort(404)

app.debug = True

if __name__ == '__main__':
    app.run()