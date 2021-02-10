from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    articles = [
        {"id": 1, "title": "Başlık1", "content": "İçerik1"},
        {"id": 2, "title": "Başlık2", "content": "İçerik2"},
        {"id": 3, "title": "Başlık3", "content": "İçerik3"}
    ]
    return render_template("index.html", articles=articles)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    # Hata mesajlarını görebilmemiz için debug true parametre verdik.
    app.run(debug=True)
