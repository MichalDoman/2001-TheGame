from flask import Flask, request
from random import randint

app = Flask(__name__)

@app.route('/2001', methods=['GET', 'POST'])
def main():
    pass


if __name__ == '__main__':
    app.run(debug=True)
