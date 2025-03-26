from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
