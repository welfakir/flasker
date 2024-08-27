from flask import Flask, render_template


# Create a flask instance
app = Flask(__name__)

# Create a reoute decorator
@app.route('/')

def index():
	first_name = "Willie"
	stuff = "This is bold text!!"
	favorite_pizza = ["Pepperoni","Cheese","Olives",41]
	return render_template("index.html",
		first_name=first_name,
		stuff=stuff,
		favorite_pizza=favorite_pizza)

# localhost:5000/user/willie
@app.route('/user/<name>')

def user(name):
	return render_template("user.html",name=name)	

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404

# Internal Server errorL
@app.errorhandler(500)
def page_not_found(e):
	return render_template("4500.html"),500