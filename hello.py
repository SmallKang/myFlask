from flask import Flask
from flask import make_response, redirect, abort
from collections import namedtuple
# from flask.ext.script import Manager
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello Wolrd!</h1>'

# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello %s!!!</h1>' % name, 400

@app.route('/response')
def response():
    response = make_response('<h1>this is a response </h1>')
    response.set_cookie('answer', '44')
    # response.set_data('hahahhahahahha')
    return response

@app.route('/redirect')
def redirect():
    return redirect('http://www.baidu.com')

def load_user(id):
    user = namedtuple('user', 'id name age')
    a = user(1, 'A', 18)
    b = user(2, 'B', 20)
    l = [a, b]
    for i in l:
        if i.id == id:
            return i

@app.route('/user/<id>')
def get_user(id):
    user = load_user(int(id))
    print(user)
    if not user:
        abort(404)
    return '<h1>Hello, %s </h1>' % user.name




if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
