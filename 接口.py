from flask import Flask, request, Response
import PyPDF2

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf' not in request.files:
        return "No file part", 400

    file = request.files['pdf']
    if file.filename == '':
        return "No selected file", 400

    if file:
        try:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            text = ''

            for page in range(num_pages):
                page_obj = reader.pages[page]
                text += page_obj.extract_text()

            # 指定返回类型为text/plain和编码为utf-8
            return Response(text, mimetype="text/plain", content_type="text/plain; charset=utf-8")

        except Exception as e:
            return str(e), 500


if __name__ == '__main__':
    app.run(debug=True)
