from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    sayi = 10
    # index.html templates klasörü altında olması gerekiyor. Flask dosya dizini oraya bakıyor.
    # number değişkenini template'e gönderdik.
    return render_template("index.html", number=sayi)


if __name__ == "__main__":
    # Hata mesajlarını görebilmemiz için debug true parametre verdik.
    app.run(debug=True)
