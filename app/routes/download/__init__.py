import os

from flask import Blueprint, send_from_directory, current_app


blueprint = Blueprint(
    'download',
    __name__,
    url_prefix='/download'
)


@blueprint.route('/<path:filename>', methods=['GET'])
def download(filename):
    return send_from_directory(
        directory=os.path.join(
            os.getcwd(),
            current_app.config['UPLOADS_FOLDER']
        ),
        filename=filename,
        as_attachment=True
    )
