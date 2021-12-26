from flask import Flask
from flask import request

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/', methods=['GET'])
def index():
    return '<html><body>index page.</body></html>\n'

@app.route('/test', methods=['GET', 'POST'])
def request_test():
    print('method=' + request.method)
    print('path=' + request.path)
    if request.method == 'POST':
        print('form data=' + request.form['foo'])
    return 'test\n'

@app.route('/person/<name>', methods=['GET'])
def hello(name):
    return 'hello ' +  name + ' !\n'

@app.route('/person', methods=['POST'])
def register():
    print(request.data)
    print(request.json['id'])
    print(request.json['name'])
    return request.data.decode() + '\n'

app.run(port=8080, debug=True)
