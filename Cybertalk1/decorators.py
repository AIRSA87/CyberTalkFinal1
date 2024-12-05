from functools import wraps
from flask import session, redirect, url_for, flash

def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Ensure the user is logged in and has the correct role
            if 'user_id' not in session or session.get('role') != role:
                flash("Access denied.", "danger")
                return redirect(url_for('auth.login'))  # Redirect unauthorized users
            return f(*args, **kwargs)
        return decorated_function
    return wrapper