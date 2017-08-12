"""View functions for app."""
from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    """."""
    context = {'headline': 'HELLOW WORLD!'}
    return render_template('index.html',
                           title='Home',
                           context=context)
