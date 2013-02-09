from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Rate My Cats'

@app.route('/submit')
def submit():
    return 'Submit Your Cat'

if __name__ == "__main__":
    app.run()

app.run(debug=True)  #Debug mode