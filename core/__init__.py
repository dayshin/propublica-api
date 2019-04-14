from flask import Flask
app = Flask(__name__)

from core.react_test.views import react_blueprint
# register the blueprints
app.register_blueprint(react_blueprint)
