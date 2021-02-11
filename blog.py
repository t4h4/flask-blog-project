from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

# Kullanıcı Kayıt Formu
class RegisterForm(Form): # Form class yapısından register form class yapısı türetiliyor. (inheritance)
    name = StringField("İsim Soyisim",validators=[validators.Length(min = 4,max = 25)])
    username = StringField("Kullanıcı Adı",validators=[validators.Length(min = 5,max = 35)])
    email = StringField("Email Adresi",validators=[validators.Email(message = "Lütfen Geçerli Bir Email Adresi Girin...")])
    password = PasswordField("Parola:",validators=[
        validators.DataRequired(message = "Lütfen bir parola belirleyin"),
        validators.EqualTo(fieldname = "confirm",message="Parolanız Uyuşmuyor...")
    ])
    confirm = PasswordField("Parola Doğrula")

# Kullanıcı Giriş Formu    
class LoginForm(Form):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Parola")

app = Flask(__name__)
app.secret_key= "blog"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "blog"
# veriler dict formatında oluyor.
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/article/<string:id>")
def detail(id):
    return "Article Id:" + id

# Register
@app.route("/register",methods = ["GET","POST"]) # GET ve POST request alabilir url.
def register():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data # formun içindeki name değerinin datası alınıp, name değerine eşitleniyor.
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data) # veri şifrelenerek alınıyor.
        # cursor mysql veritabanında işlem sağlamamızı yarayan yapı. bu yapı sayesinde sql sorgularını çalıştırabiliyoruz.
        cursor = mysql.connection.cursor() 

        sorgu = "Insert into users(name,email,username,password) VALUES(%s,%s,%s,%s)"

        cursor.execute(sorgu,(name,email,username,password))
        mysql.connection.commit() # veritabanında değişiklik yaptığımız vakit commit etmek zorundayız.

        cursor.close()
        flash("Başarıyla Kayıt Oldunuz. Lütfen Giriş Yapınız..","success") # Mesaj ve kategori flash mesajı ekrana çıkart.
        return redirect(url_for("login"))
    else:
        return render_template("register.html",form = form)

#Login işlemi
@app.route("/login",methods =["GET","POST"])
def login():
    form = LoginForm(request.form)
    return render_template("login.html", form = form)


if __name__ == "__main__":
    # Hata mesajlarını görebilmemiz için debug true parametre verdik.
    app.run(debug=True)
