# helps with the data
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from database import db, DrinkInventory, KeurigInventory, NespressoInventory, SnackInventory, OfficeSupplyInventory

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# # WARNING: This will remove all data!
# with app.app_context():
#     db.drop_all()  # This drops all tables
#     db.create_all()  # This creates them again


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
        date=datetime.now().strftime('%Y-%m-%d %I:%M %p'),
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
        date=datetime.now().strftime('%Y-%m-%d %I:%M %p'),
        half_caff=request.form['half_caff_quantity'],
        breakfast_blend=request.form['breakfast_blend_quantity'],
        breakfast_blend_decaf=request.form['breakfast_blend_decaf_quantity'],
        colombia_select=request.form['colombia_select_quantity'],
        nantucket_blend=request.form['nantucket_blend_quantity'],
        bigelow_lemon_echinacea=request.form['bigelow_lemon_echinacea_quantity'],
        swiss_miss_milk_chocolate=request.form['swiss_miss_milk_chocolate_quantity'],
        vanilla_latte=request.form['vanilla_latte_quantity'],
        chai_latte=request.form['chai_latte_quantity'],
        cafe_bustelo_dark_roast=request.form['cafe_bustelo_dark_roast_quantity'],
        mandarin_orange_spice=request.form['mandarin_orange_spice_quantity'],
        tim_hortons_original=request.form['tim_hortons_original_quantity'],
        light_roast=request.form['light_roast_quantity'],
        house_decaf=request.form['house_decaf_quantity'],
        dunkin_original_blend=request.form['dunkin_original_blend_quantity']
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
        date=datetime.now().strftime('%Y-%m-%d %I:%M %p'),
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
        date=datetime.now().strftime('%Y-%m-%d %I:%M %p'),
        baked_chips=request.form['baked_chips_quantity'],
        kirkland_snacking_nuts=request.form['kirkland_snacking_nuts_quantity'],
        kirkland_trail_mix=request.form['kirkland_trail_mix_quantity'],
        popcorn=request.form['popcorn_quantity'],
        kirkland_nut_bars=request.form['kirkland_nut_bars_quantity'],
        fruit_strips_variety_pack=request.form['fruit_strips_variety_pack_quantity'],
        cheez_it_snapped=request.form['cheez_it_snapped_quantity'],
        skinny_pop=request.form['skinny_pop_quantity'],
        nature_valley_protein_bars=request.form['nature_valley_protein_bars_quantity'],
        sun_chips=request.form['sun_chips_quantity'],
        cheez_it=request.form['cheez_it_quantity'],
        pretzels=request.form['pretzels_quantity']
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
        date=datetime.now().strftime('%Y-%m-%d %I:%M %p'),
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
