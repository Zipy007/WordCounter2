from flask import Flask, request, jsonify, render_template
from nltk.tokenize import word_tokenize
import string


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template("WC_HTML.html")


@app.route('/analyze', methods=["POST"])
def analyze():
    text = request.form['text']
    tokens = word_tokenize(text)
    words = [token for token in tokens if token.isalpha()]
    punctuation = [token for token in tokens if token in string.punctuation]
    word_count = len(words)
    punctuation_count = len(punctuation)
    return jsonify({'word_count': word_count, 'punctuation_count': punctuation_count})


if __name__ == '__main__':
    app.run(host='localhost', port=666)
