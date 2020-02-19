from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from . import main
from ..models import Pitch, User, Comment
from .forms import PitchForm, CommentForm
from .. import db

# Views
@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    title = "Home - Welcome, Pitch your ideas online"
    return render_template("index.html")


@main.route("/pitches")
@main.route("/pitches/<category>")
def pitches(category=None):
    """
    View root page function that returns the index page and its data
    """
    if not category:
        pitches = Pitch.query.all()
    else:
        pitches = Pitch.query.filter_by(category=category)

    return render_template("pitches.html", category=category, pitches=pitches)

@main.route("/pitch/new/", methods=["GET", "POST"])
@login_required
def new_pitch():
    """
    Function that creates new pitches
    """
    form = PitchForm()
    if form.validate_on_submit():
        category = form.category.data
        pitch = form.content.data

        new_pitch = Pitch(category=category, content=pitch, user=current_user)

        new_pitch.save_pitch()
        return redirect(url_for("main.index"))

    return render_template("new_pitch.html", new_pitch_form=form)




@main.route("/user/<uname>/update/pic", methods=["POST"])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if "photo" in request.files:
        filename = photos.save(request.files["photo"])
        path = f"photos/{filename}"
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for("main.profile", uname=uname))


@main.route("/user/<uname>")
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route("/user/<uname>/update", methods=["GET", "POST"])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for(".profile", uname=user.username))

    return render_template("profile/update.html", form=form)


@main.route("/pitch/comments/<int:pitch_id>", methods=["GET", "POST"])
@login_required
def view_comments(pitch_id):
    """
    Function that return  the comments belonging to a particular pitch
    """
    form = CommentForm()
    pitch = Pitch.query.filter_by(id=pitch_id).first()
    comments = Comment.query.filter_by(pitch_id=pitch.id)
    if form.validate_on_submit():
        new_comment = Comment(comment=form.comment.data, pitch=pitch, user=current_user)
        new_comment.save_comment()
        return redirect(url_for("main.view_comments", pitch_id=pitch.id))

    return render_template(
        "comments.html", pitch=pitch, comments=comments, comment_form=form
    )
