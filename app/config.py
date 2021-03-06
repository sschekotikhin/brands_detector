import os


class Config(object):
    """Класс для настройки flask приложения
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv(key='SECRET_KEY_BASE')
    UPLOADS_FOLDER = 'app/public/store'
    ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg'}


class DevelopmentConfig(Config):
    """Настройки для разработки
    """
    DEBUG = True


class StagingConfig(Config):
    """Настройки для тестового сервера
    """
    DEBUG = False


class ProductionConfig(Config):
    """Настройки для продакшена
    """
    DEBUG = False


class TestConfig(Config):
    """Настройки для тестов
    """
    TESTING = True
    DEBUG = True
