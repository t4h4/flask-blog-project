from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    # Templates klasörü altında olması gerekiyor. Flask dosya dizini oraya bakıyor.
    return render_template("index.html")


if __name__ == "__main__":
    # Hata mesajlarını görebilmemiz için debug true parametre verdik.
    app.run(debug=True)
