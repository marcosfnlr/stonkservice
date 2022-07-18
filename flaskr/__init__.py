import os

from flask import Flask


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import yfstocks
    app.register_blueprint(yfstocks.bp)

    return app
