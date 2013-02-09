from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "cats"
app.config["MONGO_HOST"] = "linus.mongohq.com"
app.config["MONGO_PORT"] = 10042
app.config["MONGO_USERNAME"] = "hello"
app.config["MONGO_PASSWORD"] = "world"
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
db = PyMongo(app)

@app.route('/')
def index():
    return 'Rate My Cats'

@app.route('/submit')
def submit():
    return 'Submit Your Cat'

if __name__ == '__main__':
    app.run()