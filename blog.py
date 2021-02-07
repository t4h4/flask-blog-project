from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    article = dict()
    article["title"] = "baslik"
    article["body"] = "icerik"
    article["author"] = "yazar"
    return render_template("index.html", article=article)


if __name__ == "__main__":
    # Hata mesajlarını görebilmemiz için debug true parametre verdik.
    app.run(debug=True)
