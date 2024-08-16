from flask import Flask, request, render_template, redirect, url_for
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form.get('text')
    dest_lang = request.form.get('dest_lang', 'en')

    if not text:
        return render_template('index.html', error='No text provided')

    translated = translator.translate(text, dest=dest_lang)
    return render_template('index.html', translated_text=translated.text)

if __name__ == '__main__':
    app.run(debug=True)
