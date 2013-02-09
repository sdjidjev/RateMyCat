from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

@app.route('/')
def index():
    return 'Rate My Cats'

@app.route('/submit')
def submit():
    return 'Submit Your Cat'

if __name__ == '__main__':
    app.run()