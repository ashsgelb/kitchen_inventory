# helps with the data
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from database import db, DrinkInventory, KeurigInventory, NespressoInventory, SnackInventory, OfficeSupplyInventory

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create or update the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def directory():
    return render_template('directory.html')

# Drink Inventory
@app.route('/drink-inventory')
def drink_inventory_page():
    items = DrinkInventory.query.all()
    return render_template('drink_inventory.html', items=items)

@app.route('/add-drink-item', methods=['POST'])
def add_drink_item():
    new_item = DrinkInventory(
        date=datetime.now().strftime('%Y-%m-%d'),
        coke=request.form['coke_quantity'],
        diet_coke=request.form['diet_coke_quantity'],
        sprite=request.form['sprite_quantity'],
        coke_zero=request.form['coke_zero_quantity'],
        lacroix_lemoncello=request.form['lacroix_lemoncello_quantity'],
        lacroix_lime=request.form['lacroix_lime_quantity'],
        lacroix_pamplemousse=request.form['lacroix_pamplemousse_quantity'],
        lacroix_pasteque=request.form['lacroix_pasteque_quantity'],
        horizon_milk=request.form['horizon_milk_quantity'],
        tangerine=request.form['tangerine_quantity'],
        lacroix_berry=request.form['lacroix_berry_quantity'],
        lemon=request.form['lemon_quantity'],
        lacroix_blackberry_cucumber=request.form['lacroix_blackberry_cucumber_quantity'],
        lacroix_cherry_lime=request.form['lacroix_cherry_lime_quantity'],
        lacroix_pineapple_strawberry=request.form['lacroix_pineapple_strawberry_quantity'],
        lacroix_ki_biscus=request.form['lacroix_ki_biscus_quantity']
    )
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('drink_inventory_page'))

@app.route('/delete-drink-item/<int:item_id>', methods=['POST'])
def delete_drink_item(item_id):
    item = DrinkInventory.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('drink_inventory_page'))

# Keurig Inventory
@app.route('/keurig-inventory')
def keurig_inventory_page():
    items = KeurigInventory.query.all()
    return render_template('keurig_inventory.html', items=items)

@app.route('/add-keurig-item', methods=['POST'])
def add_keurig_item():
    new_item = KeurigInventory(
        date=datetime.now().strftime('%Y-%m-%d'),
        keurig=request.form['keurig_quantity']
    )
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('keurig_inventory_page'))

@app.route('/delete-keurig-item/<int:item_id>', methods=['POST'])
def delete_keurig_item(item_id):
    item = KeurigInventory.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('keurig_inventory_page'))

# Nespresso Inventory
@app.route('/nespresso-inventory')
def nespresso_inventory_page():
    items = NespressoInventory.query.all()
    return render_template('nespresso_inventory.html', items=items)

@app.route('/add-nespresso-item', methods=['POST'])
def add_nespresso_item():
    new_item = NespressoInventory(
        date=datetime.now().strftime('%Y-%m-%d'),
        nespresso=request.form['nespresso_quantity']
    )
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('nespresso_inventory_page'))

@app.route('/delete-nespresso-item/<int:item_id>', methods=['POST'])
def delete_nespresso_item(item_id):
    item = NespressoInventory.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('nespresso_inventory_page'))

# Snack Inventory
@app.route('/snack-inventory')
def snack_inventory_page():
    items = SnackInventory.query.all()
    return render_template('snack_inventory.html', items=items)

@app.route('/add-snack-item', methods=['POST'])
def add_snack_item():
    new_item = SnackInventory(
        date=datetime.now().strftime('%Y-%m-%d'),
        snack=request.form['snack_name']
    )
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('snack_inventory_page'))

@app.route('/delete-snack-item/<int:item_id>', methods=['POST'])
def delete_snack_item(item_id):
    item = SnackInventory.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('snack_inventory_page'))

# Office Supply Inventory
@app.route('/office-supply-inventory')
def office_supply_inventory_page():
    items = OfficeSupplyInventory.query.all()
    return render_template('office_supply_inventory.html', items=items)

@app.route('/add-office-supply-item', methods=['POST'])
def add_office_supply_item():
    new_item = OfficeSupplyInventory(
        date=datetime.now().strftime('%Y-%m-%d'),
        office_supply=request.form['office_supply_name']
    )
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('office_supply_inventory_page'))

@app.route('/delete-office-supply-item/<int:item_id>', methods=['POST'])
def delete_office_supply_item(item_id):
    item = OfficeSupplyInventory.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('office_supply_inventory_page'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
