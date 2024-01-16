# -*- encoding: utf-8 -*-

#import os
from flask import Flask, request, render_template, jsonify
#from gevent.pywsgi import WSGIServer

app = Flask(__name__, template_folder='apps/templates', static_url_path='', static_folder='apps/static')

@app.route('/')
def index():
    return render_template('pages/index.html', segment='index')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        
        path = 'uploaded_files/'
        uploaded_files = request.files.getlist("files")

        if not uploaded_files:
            return jsonify({'message': 'No files uploaded'}), 400
        
        for file in uploaded_files:
            file.save(path+file.filename)

        return jsonify({'message': 'files uploaded'}), 200


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=4444)
