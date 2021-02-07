from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Test Flask..."

if __name__ == "__main__":
    app.run(debug=True) # Hata mesajlarını görebilmemiz için debug true parametre verdik.