from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASWORD"] = ""
app.config["MYSQL_DB"] = "flaskcontacts"

mysql = MySQL(app)

app.secret_key = "mysecretkey"


@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contacts")
    data = cur.fetchall()

    return render_template('index2.html', contacts=data)


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts(fullname,phone,email) VALUES(%s,%s,%s)",
                    (fullname, phone, email))
        mysql.connection.commit()
        flash("ñkjasjjdlnadnlkz")
        return redirect(url_for("index"))


@app.route("/edit/<id>")
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contacts WHERE id = {0} ".format(id))
    data = cur.fetchall()
    print(data[0])
    flash("ñkjasjjdlnadnlkz")
    return render_template('edit-contact.html', contacts=data[0])


@app.route("/update/<id>", methods=["POST"])
def update_contact(id):
    if request.method == "POST":
        phone = request.form["phone"]
        email = request.form["email"]
        fullname = request.form["fullname"]
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE contacts
        SET fullname = %s,
            phone = %s,
            email = %s
        WHERE id = %s
        """, (fullname, phone, email, id))
        mysql.connection.commit()
        flash("ñkjasjjdlnadnlkz")
        return redirect(url_for("index"))


@app.route("/delete/<string:id>")
def eliminar(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM contacts WHERE id = {0} ".format(id))
    mysql.connection.commit()
    flash("ñkjasjjdlnadnlkz")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=3000, debug=True)
