from flask import Flask
from core.modules.user import user_module

app = Flask(__name__)

app.register_blueprint(user_module, url_prefix='/users')

