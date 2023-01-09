from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

class Controller:
    def home(self):
        return render_template('index.html')

controller = Controller();

app.add_url_rule('/', 'index', lambda: controller.home())

if __name__ == "__main__":
    app.run(debug = True)