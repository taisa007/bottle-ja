from bottle import route, request, template, cheetah_template, jinja2_template, mako_template, run


@route('/')
def index():
    request.forms.get('test')
    return 'TOP'


@route('/hello')
def hello():
    return template('example/views/index')


@route('/default')
def default():
    return template('index')


@route('/cheetah')
def cheetah():
    return cheetah_template('cheetah')


@route('/jinja2')
def jinja2():
    name = 'jinja2'
    return jinja2_template('jinja2', name=name)


@route('/mako')
def mako():
    return mako_template('mako')


if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True, reloader=True)
