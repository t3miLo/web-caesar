from flask import Flask, render_template, url_for, redirect
from forms import CaesarForm
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Jeremiah!0!'

message = ''


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CaesarForm()
    if form.validate_on_submit():
        rot = form.rotateBy.data
        text = form.textArea.data
        global message
        message = rotate_string(text, rot)
        return redirect(url_for('caesarCypher'))
    return render_template('layout.html', form=form, legend='Caesar Cypher')


@app.route('/cypher', methods=['GET', 'POST'])
def caesarCypher():
    form = CaesarForm()
    if form.validate_on_submit():
        rot = form.rotateBy.data
        text = form.textArea.data
        global message
        message = rotate_string(text, rot)
        return redirect(url_for('caesarCypher'))
    code = message
    return render_template('cypher.html', form=form, legend='Caesar Cypher', code=code)


app.run()
