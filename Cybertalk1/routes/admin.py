from flask import Blueprint, render_template, request, redirect, url_for, flash
from Cybertalk1.cyber_db.models import Article
from Cybertalk1.cyber_db import db
from Cybertalk1.decorators import role_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')  # Example route
def admin_dashboard():
    return "Admin Dashboard"

@admin_bp.route('/articles', methods=['GET'])
@role_required("admin")
def articles_admin():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('articles_admin.html', articles=articles)

@admin_bp.route('/add_article', methods=['GET', 'POST'])
@role_required("admin")
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        author = request.form['author']
        image_url = request.form['image_url']
        new_article = Article(title=title, content=content, category=category, author=author, image_url=image_url)
        db.session.add(new_article)
        db.session.commit()
        flash("Article added successfully!", "success")
        return redirect(url_for('admin.articles_admin'))
    return render_template('add_article.html')

@admin_bp.route('/edit_article/<int:article_id>', methods=['GET', 'POST'])
@role_required("admin")
def edit_article(article_id):
    article = Article.query.get_or_404(article_id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.content = request.form['content']
        article.category = request.form['category']
        article.author = request.form['author']
        article.image_url = request.form['image_url']
        db.session.commit()
        flash("Article updated successfully!", "success")
        return redirect(url_for('admin.articles_admin'))
    return render_template('edit_article.html', article=article)

@admin_bp.route('/delete_article/<int:article_id>', methods=['POST'])
@role_required("admin")
def delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    flash("Article deleted successfully!", "success")
    return redirect(url_for('admin.articles_admin'))