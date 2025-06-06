from flask import Flask
from routes import register_blueprints

app = Flask(__name__)

register_blueprints(app)

app.run(debug=True)
