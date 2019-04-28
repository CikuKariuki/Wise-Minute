from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quote
from .forms import ReviewForm
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
def writer(writer_id):
    '''
    view function that returns the writers details page and its data
    '''
    return render_template('writer.html', id = writer_id)   
@main.route('/article_review/<int:id>', methods = ['GET','POST'])
@login_required
def article_review(id):
    article = Article.query.get_or_404(id)
    comment = Review.query.all()
    form = ReviewForm()
    
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(article.id,title,review)
        new_review.save_review()
        return redirect(url_for('arti'))