from flask import Flask
from SRC.logger import logging
from SRC.exception import CustomExcaption
import os, sys
app = Flask(__name__)

@app.route('/', methods = ["GET","PUSH"])
def index():
    try:
        raise Exception ("We are testing our exception file")
    except Exception as e:
        ML = CustomExcaption(e,sys)
        logging.info(ML.error_message)
        logging.info("WE are testing our logging file")
        return "WelCome Back"

if __name__ == "__main__":
    app.run(debug=True) 