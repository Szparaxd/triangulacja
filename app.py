from flask import Flask, render_template, request, redirect, url_for, jsonify
from main2 import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/triangulacja', methods=['POST'])
def triangulacja():
    if request.method == 'POST':
        dane = request.form['dane']

        messages = httpTringulate(dane)

        return jsonify(messages)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
