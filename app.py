from flask import Flask, render_template
from page_routes import page_routes
from models import models


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.register_blueprint(page_routes)
app.register_blueprint(models)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)