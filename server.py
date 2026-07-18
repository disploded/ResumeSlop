from flask import Flask, send_file
from generator import run
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

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