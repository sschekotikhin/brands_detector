from flask import Flask


def init(app: Flask) -> Flask:
    """Регистрирует контроллеры в приложении

    Args:
        app (Flask): приложение

    Returns:
        Flask: приложение
    """
    from app.routes.api.v1.detect import blueprint

    # blueprint для апи по распознованию картинок
    app.register_blueprint(blueprint=blueprint)

    return app
