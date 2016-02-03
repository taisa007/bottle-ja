from bottle import run, default_app

app = default_app()
run(app=app, host='localhost', port=8080, debug=True)

