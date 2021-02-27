from flask import Flask


def init(app: Flask) -> Flask:
    """Регистрирует контроллеры в приложении

    Args:
        app (Flask): приложение

    Returns:
        Flask: приложение
    """
    return app
