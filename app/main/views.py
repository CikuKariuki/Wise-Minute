from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quote
# from .forms import ReviewForm
from .. models import Review

@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    first_quote = get_quote('quote')
    title = "Home of stories"
    return render_template('index.html',title = title, quote = first_quote )
    