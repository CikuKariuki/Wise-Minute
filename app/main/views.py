from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quote
# from .forms import ReviewForm
from .. models import Review
from flask import jsonify

@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    sambu = get_quote()
    quote = sambu["quote"]
    quote_author = sambu["author"]
    title = "Home of stories"
    return render_template('index.html',title = title, quote = quote, quote_author = quote_author )

@main.route('/writer/<int:writer_id>')
def writer(id):
    '''
    view function that returns the writers details page and its data
    '''
    return render_template('writer.html', id = writer_id)   
