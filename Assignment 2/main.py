from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
db = SQLAlchemy(app)

# Define Car model
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    battery_capacity = db.Column(db.Float)
    fuel_efficiency = db.Column(db.Float)

# Create tables within the application context
with app.app_context():
    db.create_all()

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Car Inventory page
@app.route('/car_inventory')
def car_inventory():
    cars = Car.query.all()
    return render_template('car_inventory.html', cars=cars)

# Add Car page
@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        car_type = request.form['car_type']
        name = request.form['name']
        model = request.form['model']
        year = request.form['year']

        if car_type == 'Electric':
            battery_capacity = request.form['battery_capacity']
            if not battery_capacity or not battery_capacity.isdigit():
                # Handle invalid input for battery capacity
                return render_template('add_car.html', error="Invalid battery capacity value")
            new_car = Car(name=name, model=model, year=year, battery_capacity=float(battery_capacity))
        elif car_type == 'Gas':
            fuel_efficiency = request.form['fuel_efficiency']
            if not fuel_efficiency or not fuel_efficiency.isdigit():
                # Handle invalid input for fuel efficiency
                return render_template('add_car.html', error="Invalid fuel efficiency value")
            new_car = Car(name=name, model=model, year=year, fuel_efficiency=float(fuel_efficiency))
        else:
            return redirect(url_for('add_car'))

        db.session.add(new_car)
        db.session.commit()
        return redirect(url_for('car_inventory'))

    return render_template('add_car.html')


if __name__ == '__main__':
    app.run(debug=True)
