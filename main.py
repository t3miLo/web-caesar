from flask import Flask, render_template, url_for, redirect
from forms import CaesarForm, VigenereForm
from caesar import caesar_encrypt
from vigenere import vigenere_encrypt


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Jeremiah!0!0'

message = ''


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CaesarForm()
    if form.validate_on_submit():
        rot = form.rotateBy.data
        text = form.textArea.data
        global message
        message = caesar_encrypt(text, rot)
        return redirect(url_for('caesarCipher'))

    return render_template('home.html', form=form, legend='Caesar Cypher')


@app.route('/caesar', methods=['GET', 'POST'])
def caesarCipher():
    form = CaesarForm()
    if form.validate_on_submit():
        rot = form.rotateBy.data
        text = form.textArea.data
        global message
        message = caesar_encrypt(text, rot)
        return redirect(url_for('caesarCipher'))
    code = message
    return render_template('caesar.html', form=form, legend='Caesar Cipher', code=code)


@app.route('/vigenere', methods=['GET', 'POST'])
def vigenereCipher():

    form = VigenereForm()
    if form.validate_on_submit():
        keyWord = form.keyWord.data
        text = form.textArea.data
        global message
        message = vigenere_encrypt(text, keyWord)
        return redirect(url_for('vigenereCipher'))

    code = message
    return render_template('vigenere.html', form=form, legend='Vigenere Cipher', code=code)


app.run()
