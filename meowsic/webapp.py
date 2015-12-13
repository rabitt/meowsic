#!/usr/bin/env python

import sys
import os
import flask
import re
import mimetypes
from flask import Flask, render_template, request
import audio_backend
import tempfile

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['wav'])

APP = Flask(__name__)
APP.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@APP.route('/')
def index():
    return render_template('index.html')
    # return render_template('index.html', entries=entries)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def send_file_partial(path, **kwargs):
    """
        Simple wrapper around send_file which handles HTTP 206 Partial Content
        (byte ranges)
        TODO: handle all send_file args, mirror send_file's error handling
        (if it has any)
    """
    range_header = flask.request.headers.get('Range', None)
    if not range_header:
        return flask.send_file(path, **kwargs)

    size = os.path.getsize(path)
    byte1, byte2 = 0, None

    m = re.search('(\d+)-(\d*)', range_header)
    g = m.groups()

    if g[0]:
        byte1 = int(g[0])

    if g[1]:
        byte2 = int(g[1])

    length = size - byte1
    if byte2 is not None:
        length = byte2 - byte1

    data = None
    with open(path, 'rb') as f:
        f.seek(byte1)
        data = f.read(length)

    rv = flask.Response(
        data, 206, mimetype=mimetypes.guess_type(path)[0],
        direct_passthrough=True)
    rv.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(
        byte1, byte1 + length - 1, size))

    return rv


@APP.route('/api/makecatvideo', methods=['POST'])
def api_makecatvideo():
    """
    make the cat video!
    """
    if request.method == 'POST':
        upload_file = request.files['file']
        filename = upload_file.filename
        filepath = os.path.join(APP.config['UPLOAD_FOLDER'], filename)
        if upload_file and allowed_file(upload_file.filename):
            upload_file.save(filepath)

    output_file = tempfile.mkstemp(suffix='.wav')
    audio_backend.add_meow_track_to_audio(upload_file.filename, output_file)
    return send_file_partial(output_file)


if __name__ == '__main__':
    APP.run(port=5080, host='0.0.0.0', debug='--debug' in sys.argv)
