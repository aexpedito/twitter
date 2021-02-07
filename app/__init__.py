from flask import Flask

def create_app(conf_class=object):

    app = Flask(__name__)
    app.config.from_object(conf_class)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)


    return app
