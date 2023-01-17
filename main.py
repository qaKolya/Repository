from flask import Flask
import json



app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def Hello():
    return json.loads('{"message": "ok"}')

app.run()