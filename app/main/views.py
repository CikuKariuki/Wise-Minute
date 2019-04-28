from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_quote
from .forms import ReviewForm,UpdateProfile
from .. models import Review,Writer,User
from flask import jsonify
from flask_login import login_required,UserMixin,current_user
from .. import db,photos
import markdown2

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

@main.route('/article/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    article = Article.query.get_or_404(id)
    comment = Review.query.all()
    form = ReviewForm()
    
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
       # Updated review instance
        new_review = Review(article_id=article.id,article_title=title,image_path=article.poster,article_review=review,user=current_user)

        # save review method
        new_review.save_review()
        return redirect(url_for('.article',id = article.id ))

    title = f'{article.title} review'
    return render_template('new_review.html',title = title, review_form=form, article=article)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/review/<int:id>')
def single_review(id):
    review=Review.query.get(id)
    if review is None:
        abort(404)
    format_review = markdown2.markdown(review.movie_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('review.html',review = review,format_review=format_review)