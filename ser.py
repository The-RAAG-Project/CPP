from werkzeug.utils import secure_filename
from flask import Flask
import os
app = Flask(__name__)
UPLOAD_FOLDER = '/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
@app.route('/')
def index():
    return """"""

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html',name=name)

@app.route('/upload/',methods = ['GET','POST'])
def upload_file():
    if request.method =='POST':
        file = request.files['file[]']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return hello()
    return """<!doctype html>
<title>Upload new File</title>
<h1>Upload new File</h1>
<form action='' method="POST" enctype="multipart/form-data">
    <p><input type='file' name='file[]' multiple=''>
    <input type='submit' value='upload'>
    </p>

</form>"""


if __name__ == '__main__':
    app.run(port=8080)
