from flask import Blueprint, render_template, request, redirect, url_for, session, flash


general_bp = Blueprint('general', __name__, url_prefix='/general')


@general_bp.route('/')
def index():
    return render_template('home.html')

@general_bp.route('/about')
def about():
    return render_template('about.html')


@general_bp.route('/subscription')
def subscription():
    return render_template('subscriptions.html')


@general_bp.route('/features')
def features():
    return render_template('features.html')


@general_bp.route('/login')
def login():
    return render_template('login.html')


@general_bp.route('/getstarted', methods=['GET', 'POST'])
def getstarted():
    return render_template('getstarted.html')


@general_bp.route('/logout')
def logout():
    session.pop('username', None)
    flash("Logged out successfully.", "info")
    return redirect(url_for('general.index'))

