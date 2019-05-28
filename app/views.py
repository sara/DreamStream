from flask import redirect, url_for, render_template, flash, request, send_from_directory, Response

@app.route('/', methods=['GET'])
def hello():
    return "Hello World"

