import os

from flask import Flask


def init_app() -> Flask:
    """Подготавливает flask приложение к запуску

    Returns:
        Flask: flask приложение
    """
    from app import routes

    env = os.getenv('FLASK_ENV', 'development')

    app = Flask(__name__)
    app.config.from_object(f'app.config.{env.capitalize()}Config')

    app = routes.init(app)

    return app


app = init_app()
