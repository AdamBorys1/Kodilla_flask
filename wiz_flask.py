from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def about_me():
    if request.method == 'GET':
        print('We recieved GET')
        return render_template('contact.html')
    elif request.method == 'POST':
        print('We recieved POST')
        print(request.form)
        return redirect('/')