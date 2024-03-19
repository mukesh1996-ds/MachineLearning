from flask import Flask
from SRC.logger import logging

app = Flask(__name__)

@app.route('/', methods = ["GET","PUSH"])
def index():
    logging.info("WE are testing our logging file")
    return "WelCome Back"

if __name__ == "__main__":
    app.run(debug=True) 