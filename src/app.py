from dataclasses import asdict
from pathlib import Path

from flask import Flask, request, jsonify

from extractor import fetch_html, parse_products

BASE_DIR = Path(__file__).resolve().parent.parent
app = Flask(__name__, static_folder=str(BASE_DIR / "static"), static_url_path="")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/extract', methods=['POST'])
def extract():
    url = request.form.get('url')
    uploaded = request.files.get('file')

    if url:
        html = fetch_html(url)
    elif uploaded:
        html = uploaded.read().decode('utf-8')
    else:
        return jsonify({'error': 'No URL or file provided'}), 400

    products = parse_products(html)
    return jsonify([asdict(p) for p in products])

if __name__ == '__main__':
    app.run(debug=True)
