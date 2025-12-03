# app.py
from flask import Flask, render_template, request, redirect, send_from_directory, jsonify
import os
import string
import random
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
TEXT_FOLDER = 'texts'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TEXT_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TEXT_FOLDER'] = TEXT_FOLDER

def generate_room_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-room', methods=['POST'])
def create_room():
    code = generate_room_code()
    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], code), exist_ok=True)
    os.makedirs(os.path.join(app.config['TEXT_FOLDER'], code), exist_ok=True)
    return jsonify({"room_code": code})

@app.route('/room/<code>')
def room(code):
    return render_template('room.html', code=code)

@app.route('/upload/<code>', methods=['POST'])
def upload(code):
    room_path = os.path.join(app.config['UPLOAD_FOLDER'], code)
    if not os.path.exists(room_path):
        return "Room not found", 404
    for file in request.files.getlist('files'):
        filename = secure_filename(file.filename)
        file.save(os.path.join(room_path, filename))
    return 'Uploaded successfully', 200

@app.route('/files/<code>')
def files(code):
    room_path = os.path.join(app.config['UPLOAD_FOLDER'], code)
    if not os.path.exists(room_path):
        return jsonify([])
    return jsonify(os.listdir(room_path))

@app.route('/download/<code>/<filename>')
def download(code, filename):
    room_path = os.path.join(app.config['UPLOAD_FOLDER'], code)
    return send_from_directory(room_path, filename, as_attachment=True)

@app.route('/text/<code>', methods=['GET', 'POST'])
def share_text(code):
    room_path = os.path.join(app.config['TEXT_FOLDER'], code)
    file_path = os.path.join(room_path, 'shared.txt')
    if request.method == 'POST':
        content = request.json.get('content', '')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return 'Text saved', 200
    else:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return jsonify({"content": f.read()})
        return jsonify({"content": ""})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '0') in ('1', 'true', 'True')
    app.run(host='0.0.0.0', port=port, debug=debug)