from flask import Blueprint, jsonify
from flask.globals import request

from app.network import BrandsDetector

from app.utils import save_image


blueprint = Blueprint(
    'api/v1/detect',
    __name__,
    url_prefix='/api/v1/detect'
)


@blueprint.route('/', methods=['GET', 'POST'])
def detect():
    if 'images[]' not in request.files:
        return jsonify({'status': 'error'})

    result = []
    detector = BrandsDetector()
    
    for image in request.files.getlist('images[]'):
        path = save_image(image)
        result.append(detector.detect(path))

    return jsonify(result)
