from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm,UpdateProfile,PitchForm
from .. models import Reviews,User,Pitches
from flask import jsonify
from flask_login import login_required,UserMixin,current_user
from app import db

# import markdown2

@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    pitches = Pitches.query.all()

    title = "Home of stories"
    return render_template('index.html',title = title,pitches = pitches , author = current_user)

@main.route('/user/<int:user_id>')
def user(user_id):
    '''
    view function that returns the users details page and its data
    '''
    return render_template('pitches.html', id = user_id)   

@main.route("/post",methods=['GET','POST'])
@login_required
def post():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        new_post = Pitches()
        new_post.title = title
        new_post.content= content

        new_post.save_pitch()

        new_pitch = Pitches(title=title,content = content)
        reviews = Reviews.query.all()

        return redirect(url_for('main.index'))

    title="Post your pitch"
    return render_template('post.html',title=title,pitch_form=form)

@main.route("/review/<int:id>",methods=['GET','POST'])
@login_required
def review(id):
    form = ReviewForm()
    # pitch = Pitch.query.get_or_404(id)
    if form.validate_on_submit():
        review = form.review.data

        new_review = Reviews()
        new_review.review= review

        new_review.save_review()

        new_review = Reviews(review = review)

        return redirect(url_for('main.index',id = pitch.id))

    title="Post your review"
    return render_template('new_review.html',review_form=form)


# @main.route('/pitch/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_review(id):
#     form = ReviewForm()
#     # pitch = Pitch.query.get_or_404(id)
#     # comment = Review.query.all()
    
#     if form.validate_on_submit():
#         review = form.review.data
#        # Updated review instance
#         new_review = Review(review=review,user=current_user)

#         # save review method
#         new_review.save_review()
#         return redirect(url_for('.pitch',id = pitch.id ))

#     title = f'{pitch.title} review'
#     return render_template('new_review.html',review_form=form, pitch=pitch)

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

@main.route('/user/<uname>/update/pic',methods= ['POST'])
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
    review=Reviews.query.get(id)
    if review is None:
        abort(404)
    # format_review = markdown2.markdown(review.movie_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('review.html',review = review)