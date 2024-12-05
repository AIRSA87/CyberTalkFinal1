from flask import Flask, render_template
from cyber_db import init_db
from routes import admin_bp, general_bp, user_bp  # Import Blueprints from routes/__init__.py

app = Flask(__name__)

# Configure the app
app.config.from_object('instance.config.Config')

app.secret_key = 'your_secret_key'

# Initialize the database
init_db(app)

# Register the Blueprints
app.register_blueprint(general_bp, url_prefix='/general')
app.register_blueprint(admin_bp, url_prefix='/admin')  # Admin routes, prefixed with /admin
app.register_blueprint(user_bp, url_prefix='/user')    # User routes, prefixed with /user


@app.route('/')
def homepage():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

