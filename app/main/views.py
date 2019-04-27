from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quote
from .forms import ReviewForm
from .. models import Review

@main.route('/')
def index():
    