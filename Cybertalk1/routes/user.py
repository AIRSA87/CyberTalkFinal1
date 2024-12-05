from flask import Blueprint, render_template
from Cybertalk1.cyber_db.models import Article
from Cybertalk1.cyber_db import db


user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')  # User dashboard page

@user_bp.route('/forums')
def user_forums():
    return render_template('user_forums.html')  # User forums page

@user_bp.route('/articles', methods=['GET'])
def articles_user():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('user_forums.html', articles=articles)