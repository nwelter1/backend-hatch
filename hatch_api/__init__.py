from distutils.command.config import config
from flask import Flask
from config import Config
# from flask_caching import Cache
from .api.routes import api

# cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
app = Flask(__name__)
app.register_blueprint(api)
app.config.from_object(Config)
# cache.init_app(app)

