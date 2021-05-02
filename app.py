from flask import Flask, render_template, request, send_file, abort
from main import list_input, count_items, pairs_finder, write_output
from os.path import splitext
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.txt']


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            abort(400)
        filename = secure_filename(request.files['file'].filename)
        if filename != '':
            file_ext = splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            input_string = request.files['file'].read().decode('utf-8')
            input_list = list_input(input_string)
            counted_items = count_items(input_list)
            pairs = pairs_finder(counted_items)
            write_output(pairs)
        return send_file('output.txt', attachment_filename='output.txt',
                         as_attachment=True, mimetype='text/plain')
