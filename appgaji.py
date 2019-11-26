from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'perusahaan'
mysql = MySQL(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        Pendapatan = details['dapat']
        Pengeluaran = details['keluar']
        Biayaiklan = details['iklan']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO keuangan (pendapatan, pengeluaran,   biayaiklan) VALUES (%s, %s, %s)", (Pendapatan, Pengeluaran, Biayaiklan))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')
@app.route('/gaji')
def gaji():
 cur = mysql.connection.cursor()
 cur.execute('''SELECT pendapatan, pengeluaran, biayaiklan FROM keuangan''')
 rv = cur.fetchall()
 return render_template("indexgaji.html",value=rv)
if __name__ == '__main__':
    app.run()