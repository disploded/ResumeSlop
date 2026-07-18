from flask import Flask, send_file, send_from_directory
from generator import run
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

@app.route('/generate')
def generate():
    pdf_path = run()

    response = send_file(
        pdf_path,
        mimetype="application/pdf",
        as_attachment=False
    )

    @response.call_on_close
    def cleanup():
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)