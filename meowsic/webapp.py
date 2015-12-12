#!/usr/bin/env python
# import os
import sys
# import shutil
# import logging
# import tempfile
# import operator

from flask import Flask, jsonify, render_template, request

import sox
import librosa

APP = Flask(__name__)

# _CURR_DIR = os.path.dirname(__file__)
# AUDIO_DIR = os.path.join(_CURR_DIR, 'static', 'temp_audio')


@APP.route('/')
def index():
    return render_template('index.html')
    # return render_template('index.html', entries=entries)


@APP.route('/api/makecatvideo')
def api_makecatvideo():
    """
    make the cat video!
    """
    # return jsonify(transition_file=local_fpath,
    #                transition_used=transition_used)
    return None


if __name__ == '__main__':
    APP.run(port=5080, host='0.0.0.0', debug='--debug' in sys.argv)
