from flask import Flask

import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/time')
def hello():
  res = 0
  for it in range(10000000):
    res += it
  return f"""<p>Waited {res}</p>
"""

