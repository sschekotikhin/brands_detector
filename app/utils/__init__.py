from os import path
from pathlib import Path

from flask import current_app
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


def allowed_file(file: str) -> bool:
    """
    Разрешен ли указанный файл к загрузке?

    Args:
        file (str): загружаемый файл
    
    Returns:
        str: True/False
    """
    return '.' in file and \
           file.rsplit('.', 1)[1].lower() in current_app.config.get('ALLOWED_EXTENSIONS')


def save_image(image: FileStorage) -> str:
    """
    Сохраняет файл в директорию загружаемых файлов.

    Args:
        image (FileStorage): загружаемый файл

    Returns:
        str: путь до файла
    """
    # сохраняем название файла и директории
    # название директории идентично названию файла
    filename = secure_filename(image.filename)
    directory = filename.rsplit('.')[0]

    # если такой директории нет, то создаем ее
    dir_path = Path(path.join(current_app.config.get('UPLOADS_FOLDER'), directory))
    dir_path.mkdir(parents=True, exist_ok=True)

    # сохраняем файл в директорию
    image_path = path.join(
        current_app.config.get('UPLOADS_FOLDER'),
        directory,
        filename
    )
    image.save(image_path)

    return image_path
