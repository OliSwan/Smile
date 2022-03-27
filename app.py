from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def render_home():
    return render_template('home.html')


@app.route('/menu')
def render_menu():
    con = create_connection(DB_NAME)
    query= "SELECT name, description, volume, price, image FROM product"

    cur = con.cursor()
    cur.execute(query)
    product_list = cur.fetchall()
    con.close()

    return render_template('menu.html', products=product_list)


@app.route('/contact')
def render_contact():
    return render_template('contact.html')


app.run(host='0.0.0.0')
