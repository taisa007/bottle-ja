from bottle import route, request, template


@route('/')
def index():
    request.forms.get('test')
    return 'TOP'


@route('/hello')
def hello():
    return template('example/views/index')


@route('/default')
def hello():
    return template('index')
