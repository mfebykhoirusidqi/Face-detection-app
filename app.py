from flask import Flask, request, send_file, render_template
from face import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save('input.jpg')
    detect_faces('input.jpg')
    return send_file('output.jpg', mimetype='image/jpg')

if __name__ == '__main__':
    app.run(debug=True)