from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_home():
    return render_template('home.html')


@app.route('/menu')
def render_menu():
    product_list = [["Flat White", "Definitely created in New Zealand (not in the West Island) - a classic. ", "180mL", "flatwhite", "4.00"], ["Latte", "The New Zealand latte is larger than a flat white and has more foamy milk.", "240mL", "latte", "4.00"],
    ["Espresso", "Straight from the machine, 60mL including crema.", "60mL", "espresso", "3.00"],
    ["Long black", "Hot water + espresso. 120mL.", "90mL", "longblack", "3.00"]]
    return render_template('menu.html', products=product_list)


@app.route('/contact')
def render_contact():
    return render_template('contact.html')


app.run(host='0.0.0.0')
